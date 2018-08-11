from eve import Eve
from eve_sqlalchemy import SQL
from validacoes import VinculoValidator
from utils import UUIDEncoder
from hooks import validar_dados
from modelos.modelo import Base
from erros import *
import locale

from locale import setlocale

setlocale(locale.LC_ALL, "pt-BR.UTF-8")

app = Eve(validator=VinculoValidator, data=SQL, json_encoder=UUIDEncoder)

#hook que irá capturar o evento pre insert
app.on_insert += validar_dados

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

#criar a base de dados
db.create_all()

if __name__ == "__main__":
    app.run()
