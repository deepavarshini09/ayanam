from datetime import datetime


def get_current_age(birth_date_str):
    """
    Returns the exact age as a float (e.g. 18.43 years).
    birth_date_str: 'YYYY-MM-DD'

    Previously used only birth_year, which caused up to
    ~1 year error in dasha lookups.
    """

    birth_date = datetime.strptime(
        birth_date_str, "%Y-%m-%d"
    )

    today = datetime.today()

    # Full years elapsed
    years = today.year - birth_date.year

    # Check if birthday has occurred yet this year
    birthday_this_year = birth_date.replace(
        year=today.year
    )

    if today < birthday_this_year:
        years -= 1

    # Fractional part: days elapsed since last birthday
    last_birthday = birth_date.replace(
        year=today.year - (1 if today < birthday_this_year else 0)
    )

    days_since_birthday = (today - last_birthday).days

    # Use 365.25 to account for leap years
    fraction = days_since_birthday / 365.25

    return round(years + fraction, 4)


def find_current_dasha(timeline, current_age):
    """
    Finds the active Mahadasha period for the given age.
    Returns the period dict or the last period if age exceeds timeline.
    """

    for period in timeline:

        start = period["start"]
        end = period["end"]

        if start <= current_age < end:
            return period

    # If age is beyond the generated timeline,
    # return the last period rather than None
    if timeline:
        return timeline[-1]

    return None


def find_current_antardasha(antardashas, current_age):
    """
    Finds the active Antardasha period for the given age.
    Returns the period dict or the last period if age exceeds range.
    """

    for period in antardashas:

        start = period["start"]
        end = period["end"]

        if start <= current_age < end:
            return period

    # Fallback to last antardasha instead of crashing
    if antardashas:
        return antardashas[-1]

    return None