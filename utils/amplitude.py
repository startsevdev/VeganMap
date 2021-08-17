import requests
import logging


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'
BATCH_URL = 'https://api2.amplitude.com/batch'


class Amplitude:
    def __init__(self, api_key, enable=True):
        self.api_key = api_key
        self.enable = enable
        self.counter = 0
        self.request = "{"
        self.request += f'''"api_key": "{self.api_key}", '''
        self.request += '''"events": ['''
        if enable:
            logging.info("Amplitude: ON")
        else:
            logging.info("Amplitude disable")

    def send(self):
        logging.info(self.request)
        response = requests.post(BATCH_URL, data=self.request)
        logging.info(response.text)

    def log(self, user_id, event_type: str):
        if self.enable:
            if self.counter < 9:
                self.request += "{"
                self.request += f'''"user_id": {user_id}, "event_type": "{event_type}"'''
                self.request += "}, "
                self.counter += 1
            else:
                self.request += "{"
                self.request += f'''"user_id": {user_id}, "event_type": "{event_type}"'''
                self.request += "}]}"

                self.send()

                self.request = "{"
                self.request += f'''"api_key": "{self.api_key}", '''
                self.request += '''"events": ['''

                self.request += "{"
                self.request += f'''"user_id": {user_id}, "event_type": "{event_type}"'''
                self.request += "}, "

                self.counter = 1
