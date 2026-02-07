from datetime import date, datetime, timedelta
from typing import List, Dict, Optional, Union


def parse_date(date_input: Optional[Union[datetime, date, str]]) -> date:
    """
    Parse and validate date input in various formats.

    Args:
        date_input: datetime, date, string (format 'YYYY-MM-DD' or 'YYYY.MM.DD'), or None

    Returns:
        Parsed date object

    Raises:
        ValueError: If date string format is invalid
        TypeError: If date_input has unsupported type
    """
    # If None, return today's date
    if date_input is None:
        return datetime.today().date()

    # If already a datetime object, extract date
    if isinstance(date_input, datetime):
        return date_input.date()

    # If already a date object, return as is
    if isinstance(date_input, date):
        return date_input

    # If string, try to parse in both formats
    if isinstance(date_input, str):
        # Try ISO format (YYYY-MM-DD) first
        try:
            return datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            pass

        # Try dot format (YYYY.MM.DD)
        try:
            return datetime.strptime(date_input, "%Y.%m.%d").date()
        except ValueError as exc:
            raise ValueError(
                f"Invalid date format: '{date_input}'. Use 'YYYY-MM-DD' or 'YYYY.MM.DD'"
            ) from exc

    # Unsupported type
    raise TypeError(
        f"Parameter must be datetime, date, or string, got {type(date_input).__name__}"
    )


def get_upcoming_birthdays(
    users: List[Dict[str, str]], today: Optional[Union[datetime, date, str]] = None
) -> List[Dict[str, str]]:
    """
    Get list of users with birthdays in the next 7 days (including today).

    Args:
        users: List of dicts with 'name' and 'birthday' (format 'YYYY.MM.DD')
        today: Optional date object, date, or string (format 'YYYY-MM-DD' or 'YYYY.MM.DD')
               for testing (default: today's date)
    Returns:
        List of dicts with 'name' and 'congratulation_date' (format 'YYYY.MM.DD').
        If birthday falls on weekend, date is moved to next Monday.

    Example:
        >>> users = [{"name": "John Doe", "birthday": "1985.01.23"}]
        >>> get_upcoming_birthdays(users)
        [{'name': 'John Doe', 'congratulation_date': '2024.01.23'}]
    """

    # Validate input data
    if not users or not isinstance(users, list):
        return []

    # Parse and validate the 'today' parameter
    parsed_today = parse_date(today)

    upcoming = []

    # Iterate through each user in the list
    for user in users:
        # Check if user data structure is valid
        if not isinstance(user, dict) or "name" not in user or "birthday" not in user:
            continue

        try:
            # Parse birthday string into date object
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            # Get birthday date for current year
            birthday_this_year = birthday.replace(year=parsed_today.year)

            # If birthday has already passed this year, shift to next year
            if birthday_this_year < parsed_today:
                birthday_this_year = birthday_this_year.replace(
                    year=parsed_today.year + 1
                )

            # Calculate days remaining until birthday
            days_until = (birthday_this_year - parsed_today).days

            # Check if birthday falls within the next 7 days
            if 0 <= days_until < 7:
                congratulation_date = birthday_this_year

                # Move to the next working day if birthday falls on weekend
                if congratulation_date.weekday() == 5:  # Saturday
                    congratulation_date += timedelta(days=2)  # Move to Monday
                elif congratulation_date.weekday() == 6:  # Sunday
                    congratulation_date += timedelta(days=1)  # Move to Monday

                # Add user to congratulations list
                upcoming.append(
                    {
                        "name": user["name"],
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                    }
                )
        except (ValueError, KeyError):
            # Skip users with invalid data format
            continue

    return upcoming


# For testing purposes on the 07.02.2026, when 07.02.2026 is a Saturday
if __name__ == "__main__":
    USERS = [
        {"name": "John Doe", "birthday": "1985.02.07"},  # Today (Saturday)
        {"name": "Jane Smith", "birthday": "1990.02.08"},  # Tomorrow (Sunday)
        {"name": "Alice Johnson", "birthday": "1988.02.10"},  # Tuesday
        {"name": "Bob Brown", "birthday": "1992.02.14"},  # Saturday (next week)
        {"name": "Charlie Wilson", "birthday": "1995.02.06"},  # Yesterday (skip)
        {"name": "Diana Davis", "birthday": "1987.02.13"},  # Friday
    ]

    upcoming_birthdays = get_upcoming_birthdays(
        USERS, today=datetime(2026, 2, 7).date()
    )
    print("List of greetings this week:", upcoming_birthdays)

    print("\n--- New Year transition test ---")

    test_users = [
        {"name": "New Year Baby", "birthday": "1990.01.02"},
        {"name": "New Year Eve", "birthday": "1995.01.01"},
        {"name": "Early Jan", "birthday": "1988.01.05"},
        {"name": "Late Dec", "birthday": "1992.12.29"},
    ]

    result = get_upcoming_birthdays(test_users, today=datetime(2025, 12, 30).date())
    print("Result:", result)

    result_2 = get_upcoming_birthdays(test_users, today="2025-12-31")
    print("Result 2:", result_2)

    result_3 = get_upcoming_birthdays(test_users)
    print("Result 3:", result_3)
