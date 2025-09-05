"""
Configuration for cdn.
"""
# -*- coding: UTF-8 -*-


import logging
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

HOST = b'cdn.baidubce.com'
# online AK SK
AK = b'{ak}'
SK = b'{sk}'

logger = logging.getLogger('baidubce.services.cdn.cdnclient')
fh = logging.FileHandler('sample.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
config.retry_policy.max_error_retry = 0