class UserFundsService:
    def __init__(self):
        self._users_funds = {}

    def set_user_cash(self, user_id, funds):
        self._users_funds[user_id] = funds