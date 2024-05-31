from repositories.nof_repository import NofRepository

class NofService:
    def __init__(self):
        self.nof_repository = NofRepository()


    def create_nof(self, nof_data):
        self.nof_repository.create_nof(nof_data)

    def get_all_nof(self):
        return self.nof_repository.get_all_nof()
    def get_nof(self, nof_id):
        return self.nof_repository.get_nof(nof_id)

    def delete_nof(self, nof_id):
        return self.nof_repository.delete_nof(nof_id)
    