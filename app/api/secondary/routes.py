from flask_restplus import Resource
from flask import request
import random
import time

from app.api.decorators import post_response, get_response, delete_response
from app.api.secondary.models import api, request_append_model, response_apppend_model, response_get_model, \
    delete_response_model

from logger_tools import setup_logger
INMEMORY_LIST = list()

logger = setup_logger(__name__)


@api.header('Content-Type', 'application/json')
class POST(Resource):
    @api.expect(request_append_model)
    @api.response(200, 'Success', response_apppend_model)
    @post_response
    def post(self):
        global INMEMORY_LIST
        logger.info('Parsing post data')
        post_data = request.get_json(force=True, silent=True) or {}
        data = post_data.get('data')

        logger.info('Adding to memory list in master')
        delay = random.randint(10, 30)
        logger.info(f'Delay at he instance is {delay}')
        time.sleep(delay)
        INMEMORY_LIST.append(data)
        return {'status': 'success'}


@api.header('Content-Type', 'application/json')
class GET(Resource):
    @api.response(200, 'Success', response_get_model)
    @get_response
    def get(self):
        return {'status':'success', 'data': INMEMORY_LIST}

@api.header('Content-Type', 'application/json')
class Delete(Resource):
    @api.response(200, 'Success', delete_response_model)
    @delete_response
    def delete(self):
        global INMEMORY_LIST
        if not len(INMEMORY_LIST):
            logger.info('First instance not replicated')
            return {"status": "fail", "message":  f"List is empty"}

        INMEMORY_LIST.pop(-1)
        logger.info('First instance replicated')
        return {"status": "success"}
