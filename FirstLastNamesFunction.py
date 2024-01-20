def fullName(firstName, lastName):
    return firstName+lastName

def stringAlternative(fullName):
    return fullName[::2]

def main():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    name = fullName(firstName, lastName)
    print("Full name is ",name)

    result = stringAlternative(name)
    print("required string is ",result)


if __name__ == "__main__":
    main()