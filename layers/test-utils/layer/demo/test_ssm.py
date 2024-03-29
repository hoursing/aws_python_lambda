from notify.logging import Logger
import os
import boto3
import json


class SsmTest:

    def __init__(self):
        self.ssm = boto3.client('ssm')
        self.logger = Logger(os.environ.get('LOG_LEVEL', 'INFO')).get_logger()

    def get_response(self, parameter):
        if parameter is None:
            self.logger.info('Parameter is None')
            return ''

        ssm_result = self.ssm.get_parameter(Name=parameter,WithDecryption=True)['Parameter']['Value']
        return ssm_result

    def get_by_dict(self, parameter):
        if parameter is None:
            self.logger.info('Parameter is None')
            return {}

        self.logger.info('Parameter is not None')
        ssm_result = self.ssm.get_parameter(Name=parameter,WithDecryption=True)['Parameter']['Value']
        return json.loads(ssm_result)
