from repositories.data_repository import DataRepository

class DataService:
    def __init__(self):
        self.data_repository = DataRepository()

    def create_data(self, data):
        self.data_repository.create_data(data)

    def get_all_data(self):
        return self.data_repository.get_all_data()
    def get_data(self, id):
        return self.data_repository.get_data(id)

    def update_data(self, id, data):
        return self.data_repository.update_data(id, data)

    def delete_data(self, id):
        return self.data_repository.delete_data(id)
    
    # def authenticate_user(self, email, password):
    #     return self.user_repository.authenticate_user(email, password)