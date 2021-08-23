import requests
import logging
import json
import datetime
from data import config
from environs import Env


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'
BATCH_URL = 'https://api2.amplitude.com/batch'


class Amplitude:
    def __init__(self, api_key):
        self.time = datetime.datetime.now()
        self.api_key = api_key
        self.data = {"api_key": self.api_key, "events": []}

        if config.AMPLITUDE:
            logging.info(f"Amplitude: ON. Data is sent every {config.AMPLITUDE_INTERVAL} seconds")
        else:
            logging.info("Amplitude disable")

    def send_data(self):
        logging.info(self.data)
        response = requests.post(BATCH_URL, data=json.dumps(self.data))
        logging.info(response.text)

    def log(self, user_id, event_type: str):
        if config.AMPLITUDE:
            self.data["events"].append({"user_id": user_id, "event_type": event_type})

            if datetime.datetime.now() - self.time >= datetime.timedelta(seconds=config.AMPLITUDE_INTERVAL):
                self.send_data()
                self.data = {"api_key": self.api_key, "events": []}
                self.time = datetime.datetime.now()
