import sqlite3


USERFILE = "Users.db"

class Person:


    def setName(self):
        givenName = input("Enter full name")
        self.name = givenName
        return self.name

    def setAddress(self):
        givenAddress = input("Enter full address")
        self.address = givenAddress
        return self.address

    def setPhone(self):
        givenPhoneNumber = input("Enter phone number (+44)")
        self.phone = givenPhoneNumber
        return self.phone

    def setBirthday(self):
        givenBirthday = input("Enter D.O.B (dd/mm/yyyy)")
        self.birthday = givenBirthday
        return self.birthday










