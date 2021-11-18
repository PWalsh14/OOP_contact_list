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


    def action(self):
        user = input("Enter 'f' to fetch all info on users\n"
                     "Enter 'a' to add information to the database\n"
                     "Enter 's' to search for name in database\n"
                     "Enter 'u' to update table\n")
        if user == 'f':
            p1.fetchall()
        elif user == "g":
            p1.get_info()
        elif user == "s":
            p1.select()
        elif user == 'u':
            p1.update()

    def get_info(self):
        while True:
            print("Welcome to Contact manager application. If you would like to quit the app, type 'quit' as your name to close. If not, please give your details below...")
            Name = self.setName()
            if Name == "quit":
                break
            else:
                Address = self.setAddress()
                Number = self.setPhone()
                Birthday = self.setBirthday()
                conn = sqlite3.connect(USERFILE)
                c = conn.cursor()
                c.execute(
                    """
                    INSERT INTO USER(Name, Address, Phone_Number, Birthday)
                    VALUES (?,?,?,?)""", (Name, Address, Number, Birthday))
                conn.commit()
                conn.close()


    def fetchall(self):
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        query = ("""
        SELECT * FROM USER
        """)
        c.execute(query)
        fetch = c.fetchall()
        print(fetch)

    def select(self):
        name = input("Enter name to search through database").lower()
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        c.execute("""
        SELECT * FROM USER
        WHERE Name = ?""", (name,))
        user = c.fetchall()
        if user is None:
            print("contact not found")
        else:
            print(user)

    def update(self):
        contactName = input("Enter the name of the contact you would like to change").lower()
        change = input("what piece of data would you like to change?").lower()
        newChange = input("Enter new data item").lower()
        if change == 'Name':
            conn = sqlite3.connect('Users.db')
            c = conn.cursor()
            sql = ("UPDATE USER SET Name = ?" "WHERE Name = ?")
            c.execute(sql, [contactName, newChange])
            conn.commit()
            conn.close()
        elif change == 'Address':
            conn = sqlite3.connect('Users.db')
            c = conn.cursor()
            sql1 = ("UPDATE USER SET Address = ?""WHERE Address = ?")
            c.execute(sql1, [contactName, newChange])
            conn.commit()
            conn.close()
        elif change == 'Number':
            conn = sqlite3.connect('Users.db')
            c = conn.cursor()
            sql2 = ("UPDATE USER SET Phone_Number = ?""WHERE Phone_Number = ?")
            c.execute(sql2, [contactName, newChange])
            conn.commit()
            conn.close()
        elif change == 'Birthday':
            conn = sqlite3.connect('Users.db')
            c = conn.cursor()
            sql3 = ("UPDATE USER SET Birthday = ?""WHERE Birthday = ?")
            c.execute(sql3, [contactName, newChange])
            conn.commit()
            conn.close()#
        else:
            print("Option not available")

        # if change == 'Name':
        #     conn = sqlite3.connect('Users.db')
        #     c = conn.cursor()
        #     c.execute("""
        #         UPDATE USER SET Name = ?""",(newChange,))
        #     conn = sqlite3.connect('Users.db')
        #     c = conn.cursor()
        #     c.execute("""
        #         UPDATE USER SET Address = ?""", (newChange))
        # elif change == 'Number':
        #     conn = sqlite3.connect('Users.db')
        #     c = conn.cursor()
        #     c.execute("""
        #         UPDATE USER SET Phone_Number = ?""", (newChange))
        # elif change == 'Birthday':
        #     conn = sqlite3.connect('Users.db')
        #     c = conn.cursor()
        #     c.execute("""
        #         UPDATE USER SET Birthday = ?""", (newChange))
        # else:
        #     print("N/A")








p1 = Person()
p1.action()
