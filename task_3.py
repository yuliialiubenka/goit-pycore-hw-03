import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone numbers to standard format with only digits and '+'.

    Removes all non-digit characters, validates the number has exactly 10 digits
    (after removing '+' and country code '38'), and returns it in '+38...' format.

    Args:
        phone_number: Phone number string in any format

    Returns:
        Normalized phone number with '+38' country code for Ukraine (e.g., '+380501233234').
        Returns empty string if input is invalid or doesn't contain exactly 10 digits.

    Example:
        >>> normalize_phone("    +38(050)123-32-34")
        '+380501233234'
        >>> normalize_phone("+380 44 123 4567")
        '+380441234567'
        >>> normalize_phone("067 123 4567")
        '+380671234567'
    """

    if not phone_number or not isinstance(phone_number, str):
        return ""

    # Extract only digits
    digits_only = re.sub(r"\D", "", phone_number)

    # Remove country code 38 if present at the start
    if digits_only.startswith("38"):
        digits_only = digits_only[2:]

    # Validate: exactly 10 digits for local number
    if len(digits_only) != 10:
        return ""

    return "+38" + digits_only


# For testing purposes
if __name__ == "__main__":
    RAW_NUMBERS = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "3+8050 111 22 11   ",
        "+380501111 22 111",
        "+38050111122",
    ]

    sanitized_numbers = [normalize_phone(num) for num in RAW_NUMBERS]
    print("Normalized phone numbers for SMS sending:", sanitized_numbers)
