import pytest
from email_validator import email_validator

@pytest.mark.parametrize("email, expected", [
    ("a@b.com", "Valid Email."),
    ("A@b.com", "Invalid Email."),
    ("plainaddress", "Invalid Email."),
    ('"very.unusual.@.unusual.com"@example.com', "Invalid Email."),
    ("user@[192.168.0.1]", "Invalid Email."),
    ("user@.invalid.com", "Invalid Email."),
    ("user+mailbox/department=shipping@example.com", "Invalid Email."),
    ("user@[IPv6:2001:db8::1]", "Invalid Email."),
    ("Outlook Contact <outlook-contact@domain.com>", "Invalid Email."),
    ("no-tld@domain", "Invalid Email."),
    (None, "Invalid Email."),  # Test non-string input
    (123, "Invalid Email."),   # Test non-string input
    ("", "Invalid Email."),  # Empty string
    ([], "Invalid Email."),  # Non-string input
])

def test_email_validator(email, expected):
    result = email_validator(email)
    # print(result)
    assert result == expected