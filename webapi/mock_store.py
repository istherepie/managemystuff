# -- coding: utf-8 --


def get_all_the_stuff():
    """
    Retrieve all the stuff from the database

    :return: Lots of stuff (Type: list)
    """
    return [
        { "stuff": "candle", "description": "Awesome stuff" },
        { "stuff": "banana", "description": "Fruity stuff" },
        { "stuff": "Crowbar", "description": "Hard stuff" }
    ]


def get_stuff(stuff_uuid):
    """
    Get stuff from the database

    :param stuff_uuid: Object UUID (Type: uuid/str)
    :return: Content from the database (Type: dict)
    """
    return {
        "stuff": "floppy disk",
        "description": "Woobly stuff"
    }


def store_it(stuff=None):

    # Store the stuff and return the uuid

    return "e0edbf2b-cb7e-4b5f-b928-437a8fd9fc3e"


def delete(stuff_uuid):
    """
    Delete stuff from the database

    :param stuff_uuid: Object UUID (Type: uuid/str)
    :return: Success or Failure (Type: tuple)
    """

    try:
        call_delete = True

    except Exception as error:
        return (error, False)

    return (None, True)
