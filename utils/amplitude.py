import requests
import logging
from data import config


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


URL = 'https://api.amplitude.com/2/httpapi'
API_KEY = config.AMPLITUDE_API_KEY


def log_start_command(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "/start"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)


def log_help_command(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "/help"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)


def log_other(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "Other"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)


def log_location(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "Location"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)


def log_send_map(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "Open map"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)


def log_send_next(user_id):
    request_json = str({
        "api_key": API_KEY,
        "events": [{"user_id": user_id, "event_type": "Next"}]})
    response = requests.post(URL, data=request_json)
    logging.info(response.text)
