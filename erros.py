from cerberus import errors


class PtBrHandler():
    errors.ERROR_REQUIRED_FIELD = "O campo é obrigatório."
    errors.ERROR_BAD_TYPE = "O Valor informado não é aceito. {0}"
