import os
import sys
from demo.test_layer import Test
from datetime import datetime, timedelta

test = Test("Hello world DAY Report")
# ssmTest = SsmTest()

def day_handler(event, context):
    test.getName()

    time_utc = event.get('time')
    time_jst = convert_jst(time_utc)

    return 'Xin chao 12132131 TEST_LIST_PARAMETER report from AWS Lambda using Python' + sys.version + '! time '+time_jst


def convert_jst(now):
    jst_time = None
    if now:
        utc = datetime.strptime(now, '%Y-%m-%dT%H:%M:%SZ')
        jst_time = utc + timedelta(hours=9)
    return jst_time
