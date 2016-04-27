import requests
import botocore
import logging

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)

r = requests.get("https://glassfrog.holacracy.org/api/v3/roles?api_key=e741d8d9f76972ae3e720971c976b626d54d214b")

def handler(event, context):

    LOG.debug(r.text)
    LOG.debug(event)
    return {'status': 'success'}
