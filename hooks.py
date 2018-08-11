from flask import request, abort
from validacoes import VinculoValidator


def validar_dados(resource_name, items):
    VinculoValidator.validar_infomacoes(items)
