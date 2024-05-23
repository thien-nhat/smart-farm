from repositories.pump_repository import pumpRepository

class pumpService:
    def __init__(self):
        self.pump_repository = pumpRepository()

    def create_pump(self, pump_data):
        self.pump_repository.create_pump(pump_data)
    def get_pump(self, pump_id):
        return self.pump_repository.get_pump(pump_id)

    def update_pump(self, pump_id, pump_data):
        return self.pump_repository.update_pump(pump_id, pump_data)

    def delete_pump(self, pump_id):
        return self.pump_repository.delete_pump(pump_id)
    
    def authenticate_pump(self, email, password):
        return self.pump_repository.authenticate_pump(email, password)