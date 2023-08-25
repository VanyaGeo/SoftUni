import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# class MustContainOnlyNumbersAndLetters(Exception):
#     pass


email = input()

while email != "End":

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, extension = email.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = re.findall(r"\.[a-z]+", extension)
    if domain[0] not in ['.com', '.bg', '.org', '.net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    # if not name.isalnum():
    #     raise MustContainOnlyNumbersAndLetters('Name must contain only numbers and letters!')

    print("Email is valid")

    email = input()
