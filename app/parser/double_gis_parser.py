import pyshorteners
import requests

from app.core.properties import DOUBLE_GIS_API_KEY
from app.database.crud import get_reviews_count, update_reviews_count, get_review, add_reviews_count
from app.database.schemas import ReviewsCount


class DoubleGisParser:

    def __init__(self):
        self.headers = {
            'authority': 'public-api.reviews.2gis.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'origin': 'https://2gis.ru',
            'referer': 'https://2gis.ru/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36',
        }

        self.addresses = ['2393065583018885', '2393066583092767', '2393066583119255',
                          '70000001006794970', '70000001018140777', '2393065583018883',
                          '2393065583695867', '70000001057550594', '70000001044506766',
                          '70000001044506651', '70000001023134221', '70000001021885495']

        self.DOUBLE_GIS_URL = 'https://public-api.reviews.2gis.com/2.0/branches/{place_id}/reviews?limit=50&is_advertiser=false&fields=meta.providers,meta.branch_rating,meta.branch_reviews_count,meta.total_count,reviews.hiding_reason,reviews.is_verified&without_my_first_review=false&rated=true&sort_by=date_edited&key={APIKEY}&locale=ru_RU'
        self.link_to_review = ''

    def get_reviews(self):
        """
        Генераторная функиия получения списка отзывов.
        При итерации по списку отзывов, отправляет запрос на апи, после чего отправляет список отзывов
        в ранее вызванную функцию.
        Также использовалась для проверки появления новых отзывов
        """
        # self.DOUBLE_GIS_URL.format(place_id=address, APIKEY=DOUBLE_GIS_API_KEY)
        for address in self.addresses:
            yield requests.get(self.DOUBLE_GIS_URL.format(place_id=address, APIKEY=DOUBLE_GIS_API_KEY),
                               headers=self.headers).json(), address

    def get_next_reviews(self, response):
        """Проверка наличия ссылки на следующие страницы отзывов"""

        while True:
            if 'next_link' in response['meta']:
                response = requests.get(response['meta']['next_link'], headers=self.headers).json()

                for formed_response in self.generate_response(response['reviews']):
                    if formed_response is not None:
                        yield formed_response
            else:
                break

    def collect_result(self, reviews):
        """Главная генераторная функция, целью которой является генерация одного отзыва и последующей отправки пользователям"""

        for formed_response in self.generate_response(reviews['reviews']):
            if formed_response is not None:
                yield formed_response

        for next_review in self.get_next_reviews(reviews):
            yield next_review

    def generate_response(self, response):
        """
        Генераторная функция для проверки наличия отзыва в БД.
        В случае, если отзыв не найден, возвращает сформированный ответ
        """
        short = pyshorteners.Shortener()
        for item in response:

            if item['id'] != str(get_review(item['id']).id):
                yield {
                    'id': item['id'],
                    'user': (item['user']['name']),
                    'date_created': item['date_created'],
                    'rating': item['rating'],
                    'text': item['text'],
                    'website': short.tinyurl.short(self.link_to_review)
                }

    def check_new_reviews(self):
        """Проверяет отзыв на обновление"""

        for review in self.get_reviews():

            count = get_reviews_count('doublegis', place=ReviewsCount(**{
                'place_id': review[1],
                'reviews_count': review[0]['meta']['branch_reviews_count']
            }))

            if count.reviews_count == 0:
                add_reviews_count('doublegis', ReviewsCount(**{
                    'place_id': review[1],
                    'reviews_count': review[0]['meta']['branch_reviews_count']
                }))

            elif count != review[0]['meta']['branch_reviews_count']:
                update_reviews_count('doublegis', ReviewsCount(**{
                    'place_id': review[1],
                    'reviews_count': review[0]['meta']['branch_reviews_count']
                }))

            self.link_to_review = f'https://2gis.ru/ufa/search/вкусно%20и%20точка%20уфа/firm/{review[1]}/tab/reviews'
            print(self.link_to_review)
            for collect_result in self.collect_result(review[0]):
                yield collect_result
