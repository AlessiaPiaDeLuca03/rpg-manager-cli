# validators/validation.py
def is_valid_level(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False