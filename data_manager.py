class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, data):
        self.flight_data = data

    def get_Data(self):
        return self.flight_data
