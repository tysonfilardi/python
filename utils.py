from eve.io.base import BaseJSONEncoder
from uuid import UUID


class UUIDEncoder(BaseJSONEncoder):

    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        else:
            return super(UUIDEncoder, self).default(obj)