def email_validator(email: str) -> str:
    if not isinstance(email, str):
        return "Invalid Email."

    if len(email) < 7:
        return "Invalid Email."
    
    # first character must be a lower case alphabet
    if not (email[0].isalpha() and email[0].islower()):
        return "Invalid Email."

    # should be exactly one @
    if email.count("@") != 1:
        return "Invalid Email."
    
    local, domain = email.split("@")
    #domain should have exactly one . and ends with ".com" or ".in"
    if domain.count(".") != 1 or not email.endswith((".com", ".in")):
        return "Invalid Email."
    
    allowed_characters = ["_", ".", "@"]
    #checks for special characters and spaces
    for char in email:
        if char.isspace():
            return "Invalid Email."
        if not (char.isalnum() or char in allowed_characters):
            return "Invalid Email."
        
    return "Valid Email."
    