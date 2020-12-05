from pathlib import Path
from easydict import EasyDict
import os

general_config = EasyDict()
general_config.root = Path(__file__).parent

general_config.host = os.environ.get("HOST_NAME", 'localhost')
general_config.port = os.environ.get("PORT", 5001)

general_config.master_host = os.environ.get("MASTER_HOST_NAME", 'localhost')
general_config.master_port = os.environ.get("MASTER_HOST_PORT", 5000)
general_config.master_hosts = {f"{general_config.master_host}:{general_config.master_port}"}


class Config(object):
    BUNDLE_ERRORS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config_map = {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
            'production': ProductionConfig,
            'default': DevelopmentConfig
}
