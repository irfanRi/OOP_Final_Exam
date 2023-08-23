from Admin import Admin
from User import User

def main():
   tamim = User('1111', 'Belal', 'belal@gmail.com', '4321') # User
   tamim.create_account('1111', 'Belal', 'belal@gmail.com', '4321') # User
   tamim.deposit(5000)
   tamim.check_balance() # User

    kabir = User('1112', 'kabir', 'kabir@gmail.com', '4322') # User
    kabir.create_account('1112', 'kabir', 'kabir@gmail.com', '4322') # User

    
   tamim.deposit(4000) # User

   sakib = Admin('1234', 'Kuddus', 'kuddus@gmail.com', '5432') # Admin
   sakib.create_account('1234', 'Kuddus', 'kuddus@gmail.com', '5432') # Admin
   sakib.check_total_balance() # Admin

    kabir.deposit(30000) # User
    kabir.check_balance() # User

   sakib.check_total_balance() # Admin

    sakib = Admin('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.create_account('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.check_total_balance() # Admin

    kabir.check_balance() # User

    kabir.withdraw(1000) # User
    kabir.check_balance() # User

    kabir.transfer(belal, 5000) # User
   tamim.check_balance() # User

    sakib.check_transaction() # Admin
    sakib.check_total_balance() # Admin

   tamim.take_loan(5000) # User
   tamim.check_balance() # User

    sakib.check_total_balance() # Admin

    kabir.check_balance() # User

   sakib.toggle_loan_feature(False) # Admin

   tamim.take_loan(5000) # User
    kabir.take_loan(5000) # User
    kabir.check_balance() # User
   tamim.check_balance() # User

   sakib.check_total_loan() # Admin
   sakib.check_transaction() # Admin

   tamim.check_transaction_history() # User
    kabir.check_transaction_history() # User

if __name__ == '__main__':
    main()
