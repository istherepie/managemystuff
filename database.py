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

def store_it(stuff=None):

    # Store the stuff and return the uuid

    return "e0edbf2b-cb7e-4b5f-b928-437a8fd9fc3e"
