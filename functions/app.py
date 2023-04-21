import sys
from demo.test_layer import Test

test = Test("Hello world Test")

def handler(event, context):
    return 'Xin chao from AWS Lambda using Python' + sys.version + '!'
    test.getName()
