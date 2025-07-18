def email_validator():
    email = input("Enter email: ").strip() # g@g.com - minimum requirement
    is_space, invalid_char = 0, 0
    # print(f"{is_space} {invalid_char}")
    if len(email) >= 7:
        if email[0].isalpha() and email[0].islower():
            if "@" in email and email.count("@") == 1:
                domain_name = email.split("@")[1]
                # print(domain_name)
                if domain_name.count(".") == 1 and domain_name.endswith((".com", ".in")): # domain validation
                    for i in email:
                        if i.isspace():
                            is_space = 1
                        elif i.isdigit():
                            continue
                        elif i in "_@.":
                            continue
                        else:
                            invalid_char = 1
                    if is_space == 1 and invalid_char == 1: # checks special characters
                        print("Invalid Email.")
                else:
                    print("Invalid Email.")
            else:
                print("Invalid Email.")    
        else:
            print("Invalid Email.")


if __name__ == "__main__":
    # print("HEllo WOrld!")
    email_validator()