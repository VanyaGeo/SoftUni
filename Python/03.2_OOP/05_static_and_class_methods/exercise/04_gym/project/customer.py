class Customer:
    id = 1  # ->
    # Each customer should also have a personal id (autoincremented, starting from 1). To do the incrementation,
    # you should create a class attribute id equal to 1, which will keep the value of the id for the upcoming customer. For
    # example, if there are no customers, the class id should be equal to 1. When there is one customer - the class id
    # should be equal to 2.

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id

    @staticmethod
    def get_next_id():
        next_customer = Customer.id
        Customer.id += 1
        return next_customer

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


