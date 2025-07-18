import pytest
from email_validator import email_validator

@pytest.mark.parametrize("email, expected", [
    ("a@b.com", "Valid Email."),
    ("A@b.com", "Valid Email."),
    ("plainaddress", "Invalid Email."),
    ('"very.unusual.@.unusual.com"@example.com', "Valid Email."),
    ("user@[192.168.0.1]", "Valid Email."),
    ("user@.invalid.com", "Invalid Email."),
    ("user+mailbox/department=shipping@example.com", "Valid Email."),
    ("user@[IPv6:2001:db8::1]", "Valid Email."),
    ("Outlook Contact <outlook-contact@domain.com>", "Invalid Email."),
    ("no-tld@domain", "Invalid Email."),
    (None, "Invalid Email."),  # Test non-string input
    (123, "Invalid Email."),   # Test non-string input
    ("", "Invalid Email."),  # Empty string
    ([], "Invalid Email."),  # Non-string input
])

def test_email_validtor(email, expected):
    result = email_validator(email)
    return result == expected