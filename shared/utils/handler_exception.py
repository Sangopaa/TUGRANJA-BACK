from functools import wraps
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from shared.responses.dict_response import DictResponse

from models import db


def handler_service_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValidationError as err:
            return DictResponse(status_code=400, response={"error": err.messages})

        except IntegrityError as err:
            db.session.rollback()
            return DictResponse(status_code=400, response={"error": str(err.orig)})

        except Exception as e:
            return DictResponse(status_code=400, response={"error": str(e)})

    return wrapper
