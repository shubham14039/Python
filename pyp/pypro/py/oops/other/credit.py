
# import time # For taking notes of timing 
# ts = time.time()
import string

list_of_banks = [
    "State Bank of India",
    "HDFC Bank",
    "Axis Bank",
    "Kotak Mahindra Bank",
    "Punjab National Bank",
    "Bank of Baroda",
    "Canara Bank",
    "IndusInd Bank",
    "Union Bank of India"
]

# This script defines a Creditcard class to manage credit card information

class Creditcard:
    # Special Dunder methods
    def __init__(self, customer, bank, account, limit):
        """ 
        Create a creditclass instance

        The initial balance is zero
        """
        self._customer = customer  # Customer name
        self._bank = bank  # Bank name
        self._account = account  # Account number
        self._limit = limit  # Credit limit
        self._balance = 0  # Initial balance set to zero

    def __str__(self):
        # String representation of the credit card
        return str(self._customer)+ ":" + str(self._balance)

    # Getters (used to get variables set inside the class itself)
    def get_customer(self):
        """ 
        Returns the name of the customer
        Validates that the name is a non-empty string containing only letters and spaces
        """
        if not isinstance(self._customer, str) or not self._customer.strip():
            raise TypeError("The customer name must be a non-empty string")
        if not all(char in string.ascii_letters + " " for char in self._customer):
            raise ValueError("The customer name should contain only letters and spaces")
        return self._customer.strip()

    def get_bank(self):
        """ 
        Returns the name of the bank
        Validates that the bank name is in the list of valid banks
        """
        if not isinstance(self._bank, str) or not self._bank.strip():
            raise TypeError("Please choose a valid bank")
        trimmed_bank_name = self._bank.strip()
        if trimmed_bank_name not in list_of_banks:
            raise ValueError("Please choose a valid bank")
        return trimmed_bank_name

    def get_account(self):
        """
        Returns the account number of the customer
        Validates that the account number is a string of digits
        """
        if not isinstance(self._account, int):
            raise TypeError("The account number must be an integer")
        account_str = str(self._account).strip()
        if not account_str.isdigit():
            raise ValueError("Account number should contain only digits")
        return account_str

    # Setter methods (used to set new variables to self)
    def set_newname(self, new_name):
        # Method to update the customer name
        self._customer = new_name

    # Commented out methods for getting limit and balance
    # def get_limit(self):
    #     """ 
    #     Returns the Current limit of the customer
    #     """
    #     return self._limit

    # def get_balance(self):
    #     """ 
    #     Returns the current balance of the customer
    #     """
    #     return self._balance

# Example usage of the Creditcard class
c = Creditcard("Shubham", "State bank of India", 1234567876544566, 567)
print(c.get_customer())  # Prints the initial customer name
c.set_newname("kumar")  # Changes the customer name
print(c.get_customer())  # Prints the updated customer name

# Commented out example of creating another Creditcard instance
# c1 = Creditcard("12345", "State Bank of India", 1234456798767845, 10)

# ds = time.time() - ts
# print(ds, "seconds")
