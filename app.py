from eve import Eve
from eve_sqlalchemy import SQL
from validacoes import VinculoValidator
from utils import UUIDEncoder
from erros import PtBrHandler
from hooks import validar_vinculo
from modelo import Base
import locale

from locale import setlocale, LC_ALL

setlocale(locale.LC_ALL, "pt-BR")

app = Eve(validator=VinculoValidator, data=SQL, json_encoder=UUIDEncoder)

#hook que irá capturar o evento pre insert
app.on_insert += validar_vinculo

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

#criar a base de dados
# db.create_all()

if __name__ == "__main__":
    app.run()
