"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Shows information about customers in console."""

        return "<Customer: {first} {last}, {email} {pw}>".format(
            first=self.first_name, last=self.last_name,
            email=self.email, pw=self.password)


def read_customers_from_file(filepath):
    """Populates a dictionary with customer objects from data in a txt file."""

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split('|')

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_by_email(email):
    """Returns a customer by email address."""

    return customers.get(email)


customers = read_customers_from_file("customers.txt")
