from repositories.farm_repository import FarmRepository

class FarmService:
    def __init__(self):
        self.farm_repository = FarmRepository()


    def create_farm(self, farm_data):
        self.farm_repository.create_farm(farm_data)

    def get_all_farm(self):
        return self.farm_repository.get_all_farm()
    def get_farm(self, farm_id):
        return self.farm_repository.get_farm(farm_id)

    def update_farm(self, farm_id, farm_data):
        return self.farm_repository.update_farm(farm_id, farm_data)

    def delete_farm(self, farm_id):
        return self.farm_repository.delete_farm(farm_id)
    
    def authenticate_farm(self, email, password):
        return self.farm_repository.authenticate_farm(email, password)