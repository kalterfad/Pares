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

        self.addresses = ['70000001018140777', '2393065583018884', '70000001006794970', '2393065583018883',
                          '2393065583018885', '2393065583695867', '70000001021885495', '2393066583092767',
                          '2393066583119255', '70000001023134221', '70000001044506766', '70000001057550594',
                          '70000001044506651', '70000001044506349', '70000001044506283']

        self.REVIEWS_URL = 'https://flamp.ru/api/2.0/filials/{place_id}/reviews?limit=50&is_trusted=true'


    def get_reviews(self):
        response = []

        for address in self.addresses:
            response += requests.get(self.REVIEWS_URL.format(place_id=address), headers=self.headers).json()['reviews']

        return response


    def collect_result(self):

        reviews = []

        response = self.get_reviews()

        for i in response:
            reviews.append({
                'user': str(self.get_username(i['user'])),
                'date_created': i['date_created'],
                'rating': i['rating'],
                'text': i['text']
            })

        return reviews


    def get_username(self, user_id):
        return requests.get(user_id, headers=self.headers).json()['user']['name']


if __name__ == '__main__':
    print(FlampParser().collect_result())
