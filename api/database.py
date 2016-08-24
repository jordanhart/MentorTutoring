import dataset
import sqlite3



class database:
    def __init__(self):
        self.db = dataset.connect('sqlite:///tutoring.db')
        self.users = self.make_table('users')
        self.line = self.make_table('office_hours_line')
        self.review = self.make_table('review')
        self.office_hours = self.make_table('office_hours')

    def make_table(self, name):
        """
        Makes a dataset database
        >>> testDB = database()
        >>> test = testDB.make_table("testing") 
        >>> "testing" in testDB.db.tables
        True
        """
        return self.db[name]

    def add_user(self, first_name, last_name, email):
        """
        add user if doesnt exist to login database
        >>> test = database()
        >>> test.add_user("testing", "testing", "testing")
        >>> test.users.find_one(email="testing") is None
        False
        """
        if not self.users.find_one(email=email):
            self.users.insert(dict(first_name=first_name, last_name=last_name, email=email))


    def get_name_from_email(self, email):
        """
        return list of first name, last name from an email address
        >>> test = database()
        >>> test.add_user("first_name", "last_name", "email")
        >>> test.get_name_from_email("email") == ["first_name", "last_name"]
        True
        """
        return [self.users.find_one(email=email)["first_name"], self.users.find_one(email=email)["last_name"]]


    def add_office_hours(self, building, room, email):
        """
        add user if doesnt exist to office_hours database
        >>> test = database()
        >>> test.add_office_hours("testing", "testing", "testing")
        >>> test.office_hours.find_one(building="testing", room="testing") is None
        False
        """
        if not self.office_hours.find_one(building=building, room=room):
            self.office_hours.insert(dict(building=building, room=room, email=email))