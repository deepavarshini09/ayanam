from datetime import datetime


def get_current_age(birth_year):

    current_year = datetime.now().year

    return current_year - birth_year


def find_current_dasha(
    timeline,
    current_age
):

    for period in timeline:

        start = period["start"]
        end = period["end"]

        if start <= current_age < end:
            return period

    return None


def find_current_antardasha(
    antardashas,
    current_age
):

    for period in antardashas:

        start = period["start"]
        end = period["end"]

        if start <= current_age < end:
            return period

    return None