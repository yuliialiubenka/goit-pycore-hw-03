# goit-pycore-hw-03
Python. Regular expressions and advanced string manipulation.

## Project Overview
This project contains four Python functions demonstrating date manipulation, random number generation, and string processing using regular expressions.

## Functions

### Task 1: `get_days_from_today(date: str) -> int | None`
Calculates the number of days between a given date and today.

**Parameters:**
- `date` - Date string in 'YYYY-MM-DD' format

**Returns:**
- Positive number if date is in the past
- Negative number if date is in the future
- `None` if invalid format

**Example:**
```python
get_days_from_today('2022-01-22')  # Returns: 1477 (if today is 2026-02-07)
```

### Task 2: `get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list`
Generates a set of unique random numbers for lottery tickets.

**Parameters:**
- `min_num` - Minimum number (>= 1)
- `max_num` - Maximum number (<= 1000)
- `quantity` - How many numbers to generate

**Returns:**
- Sorted list of unique random integers
- Empty list if parameters are invalid

**Example:**
```python
get_numbers_ticket(1, 49, 6)  # Returns: [4, 15, 23, 28, 37, 45]
```

### Task 3: `normalize_phone(phone_number: str) -> str`
Normalizes Ukrainian phone numbers to standard format.

**Parameters:**
- `phone_number` - Phone number in any format

**Returns:**
- Normalized phone number with '+38' country code
- Empty string if invalid

**Example:**
```python
normalize_phone("    +38(050)123-32-34")  # Returns: '+380501233234'
normalize_phone("067 123 4567")           # Returns: '+380671234567'
```

### Task 4: `get_upcoming_birthdays(users: List[Dict], today: Optional[date] = None) -> List[Dict]`
Finds users with birthdays in the next 7 days and adjusts congratulation dates for weekends.

**Parameters:**
- `users` - List of dictionaries with 'name' and 'birthday' (format 'YYYY.MM.DD')
- `today` - Optional date for testing (default: today's date)

**Returns:**
- List of dictionaries with 'name' and 'congratulation_date'
- Weekend birthdays are moved to the next Monday

**Example:**
```python
users = [{"name": "John Doe", "birthday": "1985.01.23"}]
get_upcoming_birthdays(users)  # Returns: [{'name': 'John Doe', 'congratulation_date': '2024.01.23'}]
```

## Usage
Each task file can be run independently:
```bash
python task_1.py
python task_2.py
python task_3.py
python task_4.py
``` 
