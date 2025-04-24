class Passport:
    def __init__(self, passport_id, expiry_year, person_object):
        self.passport_id = passport_id
        self.expiry_year = expiry_year
        self.person = person_object

    def get_details(self):
        print(f"Passport of {self.person.get_name()} with Id : {self.passport_id} expires in {self.expiry_year}")

class Person:
    def __init__(self, person_id, name, dob, person_passport):
        self.person_id = person_id
        self.name = name
        self.dob = dob
        self.passport = person_passport

    def get_name(self):
        return self.name

    def generate_passport(self, person_passport):
        self.passport = person_passport

    def get_details(self):
        if not self.passport:
            print(f"person {self.person_id} doesn't hold a passport")
            return
        print(f"Passport details of member Id : {self.person_id} ")
        self.passport.get_details()


if __name__ == '__main__':
    person = Person("123", "Adam", "15-09-78", None)
    person.get_details()
    passport = Passport("abcd", "2047", person)
    person.generate_passport(passport)
    person.get_details()
