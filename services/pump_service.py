from repositories.pump_repository import PumpRepository
import time
# from celery import Celery


# celery = Celery('tasks', broker='pyamqp://guest@localhost//')


class PumpService:
    def __init__(self):
        self.pump_repository = PumpRepository()

    def create_pump(self, pump_data):
        self.pump_repository.create_pump(pump_data)
    def get_pump(self, pump_id):
        return self.pump_repository.get_pump(pump_id)
    def get_all_pump(self):
            return self.pump_repository.get_all_pump()
    def update_pump(self, pump_id, pump_data):
        return self.pump_repository.update_pump(pump_id, pump_data)
    
    def delete_pump(self, pump_id):
        return self.pump_repository.delete_pump(pump_id)
    # @staticmethod
    # @celery.task
    def turn_pump_on():
        PumpRepository().turn_pump_on()

    # @staticmethod
    # @celery.task
    def turn_pump_off():
        PumpRepository().turn_pump_off()

    def schedule_pump(self, start_time, end_time):
        print(time.now())
        self.turn_pump_on()
        self.turn_pump_off()
    # def authenticate_pump(self, email, password):
    #     return self.pump_repository.authenticate_pump(email, password)