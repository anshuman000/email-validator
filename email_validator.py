def email_validator(email: str) -> str:
    if not isinstance(email, str):
        print("Invalid Email.")
        return
    
    if len(email) < 7:
        print("Invalid Email.")
        return
    
    # first character must be a lower case alphabet
    if not (email[0].isalpha() and email[0].islower()):
        print("Invalid Email.")
        return

    # should be exactly one @
    if email.count("@") != 1:
        print("Invalid Email.")
        return
    
    local, domain = email.split("@")
    #domain should have exactly one . and ends with ".com" or ".in"
    if domain.count(".") != 1 or not email.endswith((".com", ".in")):
        print("Invalid Email.")
        return
    
    allowed_characters = ["_", ".", "@"]
    #checks for special characters and spaces
    for char in allowed_characters:
        if char.isspace():
            print("Invalid Email.")
            return
        if not (char.isalnum() or char in allowed_characters):
            print("Invalid Email.")
            return
        
    print("Valid Email.")
