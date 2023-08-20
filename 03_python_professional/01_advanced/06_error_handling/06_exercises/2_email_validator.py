import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

valid_domains = ['.com', '.bg', '.net', '.org']
pattern = r'(\w+)@?([a-z]+)(.[a-z]+)'
result = re.match(pattern, email)

while email != "End":
    name = result.group(1)
    domain = result.group(3)

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
