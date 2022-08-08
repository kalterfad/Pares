import pymongo

# client = MongoClient('example.com',
#                      username='user',
#                      password='password',
#                      authSource='the_database',
#                      authMechanism='SCRAM-SHA-256')

class DataBaseHandler:

    def __init__(self, collection):
        """
        Инициализирует контроллер доступа к БД

        :param collection: коллекция, к которой необходимо обратиться
        """

        # MdbURI = "mongodb://kalterfad:kalterfad'TheMurphy6512@127.0.0.1:27017/?authSource=admin"
        self.client = pymongo.MongoClient(host='localhost',
                     port=27017,
                     username='kalterfad',
                     password="6512",
                    authSource="test")

        self.data_base = self.client['Pares']

        self.collection = self.data_base[collection]


    def insert_one(self, data):
        """
        Функция записывает данные в БД

        :param data: словарь, который нужно записать
        :return:
        """
        return self.collection.insert_one(data).inserted_id


    def insert_many(self, data):
        """
        Создание несколько документов
        :param data:
        :return:
        """
        return self.collection.insert_many(data).inserted_ids


    def find_document(self, elements, multiple=False):
        """
        Функция вытаскивает документы из коллекции

        :param elements: элемент, по которому будет происходить поиск
        :param multiple: я так понял, что это множественный запрос
        :return:
        """
        if multiple:
            results = self.collection.find(elements)
            return [r for r in results]
        else:
            return self.collection.find_one(elements)


    def update_document(self, document_id, new_values):
        """
        Функция обновляет документы

        :param document_id: чат айди (айди документа) который нужно обновить
        :param new_values: новое значение элемента
        :return:
        """
        self.collection.update_one(document_id, {'$set': new_values})


    def update_many(self, document_id, new_values):
        """
        Массовое изменение документов по фильму

        :param document_id:
        :param new_values:
        :return:
        """
        self.collection.update_many(document_id, {'$set': new_values})


    def delete_document(self, document_id):
        """
        Удаление документа из коллекции

        :param document_id: айди документа, который следует удалить
        :return:
        """
        self.collection.delete_one(document_id)


    def get_all_id(self):
        """
        Функция-генератор вытаскивает все айди

        :return:
        """
        for user in self.collection.find():
            yield user