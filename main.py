from email_validator import email_validator

def main():
    try:
        email = input("Enter email: ").strip() # g@g.com - minimum requirement
        result = email_validator(email)
        print(result)
    except Exception as e:
        print(f"an error occoured {e}")
        print("Inavalid Email.")


if __name__ == "__main__":
    # print("HEllo WOrld!")
    main()