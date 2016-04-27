import boto3
import logging
import requests
from datetime import datetime

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)

r = requests.get("https://glassfrog.holacracy.org/api/v3/roles?api_key=e741d8d9f76972ae3e720971c976b626d54d214b")

def handler(event, context):
    s3 = boto3.resource('s3')
    s3.Object('kappatest', datestring).put(Body=r.content)
    
    LOG.debug(r.text)
    LOG.debug(event)
    return {'status': 'success'}
