from flask_restplus import Resource
from flask import request
import random
import time

from app.api.decorators import post_response, get_response, delete_response
from app.api.secondary.models import api, request_append_model, response_apppend_model, response_get_model, \
    delete_response_model

from logger_tools import setup_logger
INMEMORY_LIST = dict()

logger = setup_logger(__name__)


@api.header('Content-Type', 'application/json')
class POST(Resource):
    @api.expect(request_append_model)
    @api.response(200, 'Success', response_apppend_model)
    @post_response
    def post(self):
        global INMEMORY_LIST
        error_th = 0.5
        error_probability = random.uniform(0.0, 1.0)
        raise_error = error_probability > error_th
        logger.info('Parsing post data')
        post_data = request.get_json(force=True, silent=True) or {}
        data = post_data.get('data')
        key = ':'.join(data.split(':')[:-1])

        if raise_error:
            raise ConnectionError
        logger.info('Adding to memory list in secondary')
        delay = random.randint(10, 30)
        logger.info(f'Delay at he instance is {delay}')
        time.sleep(delay)
        INMEMORY_LIST[key] = data.split(':')[-1]
        logger.info(INMEMORY_LIST)
        #INMEMORY_LIST.append(data) # update append
        return {'status': 'success'}


@api.header('Content-Type', 'application/json')
class GET(Resource):
    @api.response(200, 'Success', response_get_model)
    @get_response
    def get(self):
        data = self.preproces(INMEMORY_LIST)
        logger.info(INMEMORY_LIST)
        return {'status':'success', 'data': data}

    def preproces(self, data):
        processed_data = list()
        for key, value in data.items():
            position_number, message = key.split(':')[-1], value
            processed_data.append((int(position_number), message))
        processed_data.sort(key=lambda x:x[0])
        messages = list()
        for idx, el in enumerate(processed_data):
            position_number, message = el
            if position_number == idx:
                messages.append(message)
        return messages
