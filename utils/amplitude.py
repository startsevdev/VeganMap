import requests
import logging


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'


class Amplitude:
    def __init__(self, api_key, enable=True):
        self.api_key = api_key
        self.enable = enable
        if enable:
            logging.info("Amplitude: ON")
        else:
            logging.info("Amplitude disable")

    @staticmethod
    def send(request):
        response = requests.post(URL, data=request)
        logging.info(response.text)

    def log_start_command(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "/start"}]})
            Amplitude.send(request)

    def log_help_command(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "/help"}]})
            Amplitude.send(request)

    def log_other(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "Other"}]})
            Amplitude.send(request)

    def log_location(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "Location"}]})
            Amplitude.send(request)

    def log_send_map(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "Open map"}]})
            Amplitude.send(request)

    def log_send_next(self, user_id):
        if self.enable:
            request = str({
                "api_key": self.api_key,
                "events": [{"user_id": user_id, "event_type": "Next"}]})
            Amplitude.send(request)
