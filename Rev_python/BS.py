class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
            
        try:
            
            if amount < 0:
                raise ValueError("ValuError")
            elif amount> self.balance:
                raise InsufficientFundsError("Insufficient funds") 
            else:
                self.balance -= amount
                return self.balance
        except ValueError:
            # TODO: Handle negative withdrawal amounts
            return "Error: ValueError"
        except InsufficientFundsError:
                # TODO: Handle insufficient funds
                return "Error: Insufficient funds"
                
        except Exception as e:
                # TODO: Handle unexpected errors
                return "An unexpected error occurred"
# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
print(account.withdraw(50))  # Should succeed and print remaining balance
