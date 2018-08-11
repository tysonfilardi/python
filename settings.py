from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from modelos.modelo import Pacientes

DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@localhost:5432/criare'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

DOMAIN = DomainConfig({
    'pacientes': ResourceConfig(Pacientes),
}).render()
