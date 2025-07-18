# Email Validator

This project provides a Python-based email validator that checks whether an email address meets the minimum requirements based on RFC 5322 standards. The validator is implemented as a pure function, making it easy to test and integrate into other applications.

## Features

- Validates email addresses according to a practical subset of RFC 5322.
- Returns a clear result: `"Valid Email."` or `"Invalid Email."`.
- Handles exceptions and non-string inputs gracefully.

## Usage

### As a Script

Run the main program to validate an email address via command line:

```bash
python main.py
```

You will be prompted to enter an email address, and the validator will output whether it is valid or not.

### As a Library

You can import and use the validator function in your own Python code:

```python
from email_validator import email_validator

result = email_validator("example@domain.com")
print(result)  # "Valid Email."
```

## Testing

This project uses `pytest` for testing. To run the tests:

```bash
pytest
```

Test file included:

- `test_email_validator.py`

## File Overview

- `main.py`
- `email_validator.py`
- `test_email_validator.py`

## Exception Handling

- The validator handles non-string inputs and unexpected exceptions by returning `"Invalid Email."` instead of raising errors.

## Requirements

- Python 3.6+
- `pytest` (for running tests)

Install dependencies with:

```bash
pip install pytest
```

## License

This project is open-source.
