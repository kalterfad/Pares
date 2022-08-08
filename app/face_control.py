class Controller:
    """Декоратор класса для проверки message_id"""

    def __init__(self, list_name):

        self.list_name = list_name

        self.dict_id = {
            'ban': [],
            'admin': ['446777294']
        }

        self.checking_case = {
            'ban': self.checking_ban_list,
            'admin': self.checking_admin_list
        }


    def __call__(self, func):

        def wrapper(*args, **kwargs):
            condition = self.checking_case[self.list_name]
            if condition(*args, id_dict=self.list_name):
                result = func(*args, **kwargs)

                return result
        return wrapper


    def checking_ban_list(self, message, id_dict):
        if str(message.chat.id) not in self.dict_id[id_dict]:
            return True
        else:
            return False


    def checking_admin_list(self, message, id_dict):
        if str(message.chat.id) in self.dict_id[id_dict]:
            return True
        else:
            return False