import datetime
from repositories.pump_repository import PumpRepository
import time
from apscheduler.schedulers.background import BackgroundScheduler

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

    # def schedule_pump(self, start_time, end_time):
    #     print(time.now())
    #     self.turn_pump_on()
    #     self.turn_pump_off()
    def schedule_pump(self, start_time, end_time):
        # Convert the start_time and end_time from string to datetime
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
        end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")

        # Initialize the scheduler
        scheduler = BackgroundScheduler()

        # Schedule the pump to turn on at the start_time
        scheduler.add_job(self.pump_repository.turn_pump_on, 'date', run_date=start_time, misfire_grace_time=36)

        # Schedule the pump to turn off at the end_time
        scheduler.add_job(self.pump_repository.turn_pump_off, 'date', run_date=end_time, misfire_grace_time=36)

        # Start the scheduler
        scheduler.start()

    def check_and_turn_on_pump(self, pump_id, soil_moisture):
        pump = self.get_pump(pump_id)
        # print(pump[3])
        # print(type(pump['status']))  # Fix: Replace typeof with type
        # print(soil_moisture)

        if pump[3] and 30 <= soil_moisture <= 70:
            self.pump_repository.turn_pump_on()
        else:
            self.pump_repository.turn_pump_off()
    # def authenticate_pump(self, email, password):
    #     return self.pump_repository.authenticate_pump(email, password)