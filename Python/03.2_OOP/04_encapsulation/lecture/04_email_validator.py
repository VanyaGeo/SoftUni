class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, email) -> bool:
        info = email.split("@")
        name = info[0]
        ending = info[1].split(".")
        mail = ending[:-1]
        domain = ending[-1]

        return self.__is_name_valid(name) and self.__is_mail_valid(*mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domain)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


