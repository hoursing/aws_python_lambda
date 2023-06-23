import sys
import pandas as pd

def handler(event, context):
    pd.DataFrame({'A': [1, 2, 3]})
    return 'Xin chao from AWS Lambda using Python' + sys.version + '!'
