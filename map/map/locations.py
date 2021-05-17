""" locations.py

Place labels to objects on the map.

"""

from .config import config


def get_things():
    return config.get("things")


things = get_things()


def get_locations(things=None):
    """Read the locations in the configuration file.
    """
    if not things:
        return list(map(lambda thing: thing['location'], things))
    return [thing['location'] for thing in things]