import json
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    return {
        'statusCode': 200,
        'body': json.dumps(f'Current time: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    }
