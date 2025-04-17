# Use the techniques of exeption handling to revise the add_balance and make_payment methods of creditclass to ensure that the user sends a number as a parameter
# 
# It is also ensured that add_balance accept POSITIVE number as a parameter as in r205.py


class CreditCard:
    def __init__(self, customer, bank, acnt, limit) -> None:
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    
    def __str__(self) -> str:
        return f"Customer: {self._customer},Bank: {self._bank}, Account No.: {self._account}, Balance: {self._balance}, Limit: {self._limit}" 
    
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
        
    
    
    def add_balance(self, money: int):
        '''
        Add balance to the customers' account
        '''
        try:
            if not isinstance(money, (int,float)):
                raise TypeError("Amount must be a number")
            if not money >=0:
                raise ValueError("Amount must be a positive number")
            self._balance += money
            return True
        
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
            return False
        
        
    
    def make_payment(self, amount):
        try:
            if not isinstance(amount,(int,float)):
                raise TypeError("Amount must be a number")
            
            self._balance -= amount
            
        except TypeError as e:
            print(f"Error: {e}")


customer = CreditCard("Shubham Kumar", "State Bank of India", 9872939382827337, 9000)


print(customer.add_balance(-900))
print(customer.get_balance())
