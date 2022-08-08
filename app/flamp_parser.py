import requests

from app.core.properties import FLAMP_API_KEY


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

    def get_reviews(self, link) -> list:

        for address in self.addresses:
            yield requests.get(link.format(place_id=address), headers=self.headers).json()

    def generate_response(self, response):
        for item in response:
            if item['id'] != 2:
                yield {
                    'id': item['id'],
                    'user': str(self.get_username(item['user'])),
                    'date_created': item['date_created'],
                    'rating': item['rating'],
                    'text': item['text']
                }

    def collect_result(self):

        for response in self.get_reviews(self.REVIEWS_URL):

            for formed_response in self.generate_response(response['reviews']):
                if formed_response is not None:
                    yield formed_response

            for next_review in self.get_next_reviews(response):
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

        for review in self.get_reviews(self.REVIEW_COUNT_URL):
            # if review['filial']['reviews_count']:
            print(review['filial']['reviews_count'])


if __name__ == '__main__':
    c = 0
    for i in FlampParser().collect_result():
        print(i)
        c += 1

    print(c)
