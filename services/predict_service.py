from repositories.predict_repository import PredictRepository

class PredictService:
    def __init__(self):
        self.predict_repository = PredictRepository()

    def create_predict(self, predict_data):
        self.predict_repository.create_predict(predict_data)
    def get_all_predict(self):
        return self.predict_repository.get_all_predict()
    def get_predict(self, predict_id):
        return self.predict_repository.get_predict(predict_id)
