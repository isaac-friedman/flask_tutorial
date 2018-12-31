import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'there will be a 128-bit random string here at some point'
    TESTING = True
    
