from __init__ import CONN, CURSOR
import random
from restaurant import Restaurant
from customer import Customer
from review import Review
import ipdb


def reset_database():
    Review.drop_table()
    Customer.drop_table()
    Restaurant.drop_table()
    Restaurant.create_table()
    Customer.create_table()
    Review.create_table()

    # Create seed data
    kempinski = Restaurant.create("Kempinski", 100)
    kibandanski = Restaurant.create("Kibandanski", 20)
    customer1 = Customer.create("Lee", "Bruce")
    customer2 = Customer.create("Sasha", "Obama")
    Review.create(1, 1, 3)
    Review.create(1, 2, 4)
    Review.create(2, 2, 5)


reset_database()
ipdb.set_trace()