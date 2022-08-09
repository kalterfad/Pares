import requests

from app.core.properties import FLAMP_API_KEY
from app.crud import get_reviews_count, update_reviews_count, get_review
from app.schemas import ReviewsCount


class FlampParser:

    def __init__(self):
        self.headers = {
            'X-Application': 'Flamp4',
            'Origin': 'https://ufa.flamp.ru/',
            'Authorization': FLAMP_API_KEY,
            'Accept': ';q=1;depth=0;scopes={};application/json',
            'Referer': 'https://ufa.flamp.ru/',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        self.addresses = ['2393065583018884', '70000001018140777', '70000001006794970', '2393065583018883',
                          '2393065583018885', '2393065583695867', '70000001021885495', '2393066583092767',
                          '2393066583119255', '70000001023134221', '70000001044506766', '70000001057550594',
                          '70000001044506651', '70000001044506349', '70000001044506283']

        self.REVIEWS_URL = 'https://flamp.ru/api/2.0/filials/{place_id}/reviews?limit=5'
        self.REVIEW_COUNT_URL = 'https://flamp.ru/api/2.0/filials/{place_id}'

    def get_reviews(self, link):

        for address in self.addresses:
            yield requests.get(link.format(place_id=address), headers=self.headers).json(), address

    def generate_response(self, response):
        """
       Генераторная функция для проверки наличия отзыва в БД.
       В случае, если отзыв не найден, возвращает сформированный ответ
       """
        for item in response:

            if item['id'] != get_review(item['id']).id:
                yield {
                    'id': item['id'],
                    'user': str(self.get_username(item['user'])),
                    'date_created': item['date_created'],
                    'rating': item['rating'],
                    'text': item['text']
                }

    def collect_result(self, review_link):

        for response in self.get_reviews(review_link):

            for formed_response in self.generate_response(response[0]['reviews']):
                if formed_response is not None:
                    yield formed_response

            for next_review in self.get_next_reviews(response[0]):
                yield next_review

    def get_next_reviews(self, response):
        """Проверка наличия ссылки на следующие страницы отзывов"""

        while True:

            if 'next_link' in response:
                # re.search('offset_id.*?(\d+)', response['next_link']).group(1)
                response = requests.get(f"{response['next_link']}", headers=self.headers).json()

                for formed_response in self.generate_response(response['reviews']):
                    if formed_response is not None:
                        yield formed_response
            else:
                break

    def get_username(self, user_id: str):
        return requests.get(user_id, headers=self.headers).json()['user']['name']

    def check_new_reviews(self):
        """
        Проверка на появление новых отзывов
        В случае если появился новый отзыв, нужно запускать метод парсинга отзывов
        """
        for review in self.get_reviews(self.REVIEW_COUNT_URL):

            count = get_reviews_count('flamp', place=ReviewsCount(**{
                'place_id': review[0]['filial']['id'],
                'reviews_count': review[0]['filial']['reviews_count']
            }))

            if count.reviews_count != review[0]['filial']['reviews_count']:
                update_reviews_count('flamp', ReviewsCount(**{
                    'place_id': review[0]['filial']['id'],
                    'reviews_count': review[0]['filial']['reviews_count']
                }))

                for collect_result in self.collect_result(self.REVIEWS_URL):
                    yield collect_result



if __name__ == '__main__':

    c = 0
    FlampParser().check_new_reviews()


