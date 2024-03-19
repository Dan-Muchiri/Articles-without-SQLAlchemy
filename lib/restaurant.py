# lib/department.py
from __init__ import CURSOR, CONN


class Restaurant:
    
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.price}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price
        else:
            raise ValueError(
                "Price must be an integer."
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Restaurant instances """
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Restaurant instances """
        sql = """
            DROP TABLE IF EXISTS restaurants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Restuarant instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO restaurants (name, price)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price):
        """ Initialize a new Restaurant instance and save the object to the database """
        restaurant = cls(name, price)
        restaurant.save()
        return restaurant

 