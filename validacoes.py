from eve_sqlalchemy.validation import ValidatorSQL
from flask import abort
# from erros import PtBrHandler


class VinculoValidator(ValidatorSQL):

    def validar_infomacoes(json_items):
        print(json_items)


