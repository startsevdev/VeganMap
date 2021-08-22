import requests
import logging
import json
import datetime


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'
BATCH_URL = 'https://api2.amplitude.com/batch'

TIMEDELTA = datetime.timedelta(seconds=30)


class Amplitude:
    def __init__(self, api_key, enable=True):
        self.api_key = api_key
        self.enable = enable
        self.data = {"api_key": self.api_key, "events": []}
        self.time = datetime.datetime.now()

        if enable:
            logging.info("Amplitude: ON")
        else:
            logging.info("Amplitude disable")

    def send_data(self):
        logging.info(self.data)
        response = requests.post(BATCH_URL, data=json.dumps(self.data))
        logging.info(response.text)

    def log(self, user_id, event_type: str):
        if self.enable:
            self.data["events"].append({"user_id": user_id, "event_type": event_type})

            if datetime.datetime.now() - self.time >= TIMEDELTA:
                self.send_data()
                self.data = {"api_key": self.api_key, "events": []}
                self.time = datetime.datetime.now()
