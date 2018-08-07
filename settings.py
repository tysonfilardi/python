from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from modelo import Vinculos

DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@localhost:5432/criare20'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = DomainConfig({
    'vinculos': ResourceConfig(Vinculos),
}).render()
