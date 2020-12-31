import traceback
from collections import Mapping
from logger_tools import setup_logger
import sys

logger = setup_logger(__name__)


def get_response(f):
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except:
            logger.exception("Fatal error during processing.")
            result = {'status': 'fail',
                      'message': f'Something went wrong - {traceback.format_exc()}'}, 500
        return result
    return wrapped


def post_response(f):
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except:
            logger.exception("Fatal error during processing.")
            result = {'status': 'fail',
                      'error': f'{traceback.format_exc()}',
                      'message': f'Something went wrong - {traceback.format_exc()}'}, 500
        return result
    return wrapped


def delete_response(f):
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except:
            logger.exception("Fatal error during processing.")
            result = {'status': 'fail',
                      'message': f'Something went wrong - {traceback.format_exc()}'}, 500
        return result
    return wrapped
