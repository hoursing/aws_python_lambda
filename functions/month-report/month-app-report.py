import sys


def handler(event, context):
    return 'Xin chao from AWS Lambda using Python' + sys.version + '!'
