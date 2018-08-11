from eve_sqlalchemy.validation import ValidatorSQL
from datetime import datetime
from flask import abort
# from erros import PtBrHandler


class VinculoValidator(ValidatorSQL):

    def validar_maioridade(dt_nasc):
        now = (datetime.now())
        print(now.year)
        print(now.month)
        print(now.day)
        print(type(dt_nasc))




    def validar_infomacoes(json_items):
        VinculoValidator.validar_maioridade(json_items[0]['dt_nasc'])
        print(json_items[0]['cpf'])
        print(json_items[0]['nome'])
        print()





