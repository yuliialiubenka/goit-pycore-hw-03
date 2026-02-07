from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Calculate the number of days between a given date and today.

    Args:
        date: Date string in 'YYYY-MM-DD' format (e.g., '2026-01-01')

    Returns:
        Number of days from the given date to today:
        - Positive: date is in the past
        - Negative: date is in the future
        - None: invalid date format or empty string

    Example:
        >>> get_days_from_today('2022-01-22')
        1477  # if today is 2026-02-07
    """

    if not date or not isinstance(date, str):
        return None
    try:
        given_date = datetime.strptime(date.strip(), "%Y-%m-%d").date()
        today = datetime.today().date()

        return (today - given_date).days
    except (ValueError, AttributeError):
        return None


# For testing purposes
if __name__ == "__main__":
    TEST_DATE = "2022-01-22"

    print(get_days_from_today(TEST_DATE))
