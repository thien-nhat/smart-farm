from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        self.user_repository.create_user(user_data)
    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id, user_data):
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)
    
    def authenticate_user(self, email, password):
        return self.user_repository.authenticate_user(email, password)