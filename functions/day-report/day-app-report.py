import os
import sys
from demo.test_layer import Test
from demo.test_ssm import SsmTest

test = Test("Hello world DAY Report")
ssmTest = SsmTest()

def day_handler(event, context):
    test.getName()

    ssmTest.get_by_dict(os.getenv('TEST_LIST_PARAMETER'))
    return 'Xin chao TEST_LIST_PARAMETER report from AWS Lambda using Python' + sys.version + '!'
