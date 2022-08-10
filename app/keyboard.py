from keyboa import Keyboa


class Keyboard:

    def __init__(self, chat_id, is_active_actions, is_superuser_actions):
        self.chat_id = chat_id
        self.is_active_actions = is_active_actions
        self.is_superuser_actions = is_superuser_actions


    def user_right_keyboard(self):


        executor_button = [
            [
                {self.is_active_actions: f'is_active_id{self.chat_id}'},
                {self.is_superuser_actions: f'is_superuser_id{self.chat_id}'}
            ]
        ]

        return Keyboa(items=executor_button).keyboard

