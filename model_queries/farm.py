from models import db

from models.farm import Farm


def get_farm_by_id(farm_id: int) -> Farm:
    """Obtain a farm by its ID.

    Keyword arguments:
        farm_id -- ID of the farm to be obtained.
    Return:
        Farm object with the given ID.
    """

    return db.session.query(Farm).filter(Farm.identifier == farm_id).one_or_none()


def get_paginated_farms(page: int, size: int) -> list[Farm]:
    """Obtain a paginated list of farms.

    Keyword arguments:
        page -- Page number to retrieve.
        size -- Number of farms per page.
    Return:
        List of Farm objects for the given page.
    """

    return db.session.query(Farm).paginate(page=page, per_page=size).items
