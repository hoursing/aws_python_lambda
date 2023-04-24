import sys
from demo.test_layer import Test

test = Test("Hello world MONTH report")

def handler(event, context):
    test.getName()
    return 'Xin chao from AWS Lambda using Python' + sys.version + '!'
