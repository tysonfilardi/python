from eve_sqlalchemy.validation import ValidatorSQL
from flask import abort
# from erros import PtBrHandler


class VinculoValidator(ValidatorSQL):

    # def __init__(self):
    #     self.__error_handler = PtBrHandler()

    def validar_vinculo(json_items):
        print("chegou aqui")

