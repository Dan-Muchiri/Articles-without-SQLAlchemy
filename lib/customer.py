# lib/department.py
from __init__ import CURSOR, CONN


class Customer:
    
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.first_name}, {self.last_name}>"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name):
            self._first_name = first_name
        else:
            raise ValueError(
                "First name must be a non-empty string"
            )

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):  # Corrected method name to 'last_name'
        if isinstance(last_name, str) and len(last_name):
            self._last_name = last_name
        else:
            raise ValueError(
                "Last name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Customer instances """
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Customer instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name):
        """ Initialize a new Customer instance and save the object to the database """
        customer = cls(first_name, last_name)
        customer.save()
        return customer

