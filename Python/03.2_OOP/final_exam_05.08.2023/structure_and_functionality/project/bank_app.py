from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPES = {"Student": "StudentLoan", "Adult": "MortgageLoan"}

    def __init__(self, capacity: int):
        self.capacity = capacity  # number of clients
        self.loans = []  # objects
        self.clients = []  # objects

    def add_loan(self, loan_type: str):
        if loan_type == "StudentLoan":
            loan = StudentLoan()
        elif loan_type == "MortgageLoan":
            loan = MortgageLoan()
        else:
            raise Exception("Invalid loan type!")

        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type == "Student":
            client = Student(client_name, client_id, income)
        elif client_type == "Adult":
            client = Adult(client_name, client_id, income)
        else:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id][0]
        loan = [l for l in self.loans if isinstance(l, StudentLoan if loan_type == "StudentLoan" else MortgageLoan)][0]
                # l.__class__.__name__ == loan_type]
        if not loan.__class__.__name__ == self.VALID_TYPES[client.__class__.__name__]:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]
        if client:
            client = client[0]
        else:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans_amount = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans_amount += 1

        return f"Successfully changed {changed_loans_amount} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients_amount = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients_amount += 1

        return f"Number of clients affected: {changed_clients_amount}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_income = sum(client.income for client in self.clients)

        # granted_loans = [loan for client in self.clients for loan in client.loans]
        granted_loans = []
        for client in self.clients:
            for loan in client.loans:
                granted_loans.append(loan)

        loans_count_granted_to_clients = len(granted_loans)
        granted_sum = sum(loan.amount for loan in granted_loans)

        available_loans = [loan for loan in self.loans]
        loans_count_not_granted = len(available_loans)
        not_granted_sum = sum(loan.amount for loan in available_loans)

        total_interest = sum(client.interest for client in self.clients)
        avg_client_interest_rate = total_interest / active_clients if active_clients > 0 else 0.0

        return (
            f"Active Clients: {active_clients}\n"
            f"Total Income: {total_income:.2f}\n"
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        )



