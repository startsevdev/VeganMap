import requests
import logging
from data import config


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'
API_KEY = config.AMPLITUDE_API_KEY


class Amplitude:
    def __init__(self, api_key):
        self.api_key = api_key

    def log_start_command(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "/start"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)

    def log_help_command(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "/help"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)

    def log_other(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "Other"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)

    def log_location(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "Location"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)

    def log_send_map(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "Open map"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)

    def log_send_next(self, user_id):
        request_json = str({
            "api_key": self.api_key,
            "events": [{"user_id": user_id, "event_type": "Next"}]})
        response = requests.post(URL, data=request_json)
        logging.info(response.text)
