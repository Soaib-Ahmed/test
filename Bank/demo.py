import random
class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 2
    
    users = []
    loan_enabled = True
    is_bankrupt = False

    @staticmethod
    def generate_account_number():
        return random.randint(10000, 99999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: +{amount}')
            return True
        else:
            print("Invalid deposit amount")
            return False

    def withdraw(self, amount):
        if User.is_bankrupt:
            print("Bank is bankrupt. Withdrawal not allowed.")
            return False

        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -{amount}')
            return True
        else:
            print("Withdrawal amount exceeded")
            return False

    def check_balance(self):
        return self.balance

    def transfer(self, other_user, amount):
        if User.is_bankrupt:
            print("Bank is bankrupt. Transfer not allowed.")
            return False

        if self.balance >= amount and other_user is not None:
            self.balance -= amount
            other_user.balance += amount
            self.transaction_history.append(f'Transfer: -{amount}')
            other_user.transaction_history.append(f'Transfer: +{amount}')
            return True
        else:
            print("Transfer failed. Account does not exist or insufficient balance.")
            return False

    def take_loan(self, amount):
        if User.is_bankrupt:
            print("Bank is bankrupt. Loan not allowed.")
            return False

        if User.loan_enabled and self.loan_count > 0 and self.balance >= amount and amount <= 10000:
            self.balance += amount
            self.loan_count -= 1
            self.transaction_history.append(f'Loan: +{amount}')
            return True
        elif not User.loan_enabled:
            print("Loan feature is currently disabled.")
            return False
        elif self.loan_count <= 0:
            print("You can't take a loan after 2 times.")
            return False
        elif amount > 10000:
            print("Loan amount must be under 10,000 Tk.")
            return False
        else:
            print("Loan request denied.")
            return False

    def show_transaction_history(self):
        return self.transaction_history

    @staticmethod
    def user_exists(account_number):
        for user in User.users:
            if user.account_number == account_number:
                return user
        return None

class Admin(User):
    def __init__(self):
        super().__init__("Admin", "admin@example.com", "Admin Address", "Admin")
    
    def admin_login(self):
        # Simple admin login with username and password
        username = input("Admin Username: ")
        password = input("Admin Password: ")
        return username == "admin" and password == "admin123"

    def create_account(self, name, email, address, account_type):
        user = BankUser(name, email, address, account_type)
        User.users.append(user)

    def delete_user_account(self, account_number):
        user = User.user_exists(account_number)
        if user:
            User.users.remove(user)
        else:
            print("Account does not exist.")

    def view_user_accounts(self):
        for user in User.users:
            print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in User.users)
        return total_balance

    def check_total_loan_amount(self):
        total_loan = sum(user.balance for user in User.users if user.balance < 0)
        return abs(total_loan)

    def toggle_loan_feature(self, enable):
        User.loan_enabled = enable

    def toggle_bankrupt_status(self, is_bankrupt):
        User.is_bankrupt = is_bankrupt
current_user = None
while True:
    if current_user is None:
        print('\nNO User Login!\n')
        choice = input("Login or Register (L/R/A): ")
        if choice == 'R':
            name = input('Name: ')
            email = input('Email: ')
            address = input('Address: ')
            account_type = input('Account Type (Savings/Current): ').capitalize()

            if account_type not in ['Savings', 'Current']:
                print('Invalid Account Type\n')
                continue

            current_user = User(name, email, address, account_type)
            User.users.append(current_user)  # Add the newly registered user to the list
            print(f'Account successfully registered!\nAccount Number: {current_user.account_number}')
        elif choice == 'L':
            try:
                account_number = int(input('Account Number: '))
            except ValueError:
                print('Invalid account number. Please enter a valid number.')
                continue

            current_user = User.user_exists(account_number)
            if not current_user:
                print('Account does not exist.\n')
                continue
        elif choice == 'A':
            if User.admin_login():
                admin_menu = input("Admin Menu: 1. Create Account, 2. Delete User Account, 3. Toggle Loan Feature, 4. View User Accounts, 5. Check Total Balance, 6. Check Total Loan Amount, 7. Toggle Bankrupt Status, 8. Logout. Enter your choice: ")
                if admin_menu == "1":
                    name = input("Enter User's Name: ")
                    email = input("Enter User's Email: ")
                    address = input("Enter User's Address: ")
                    account_type = input("Enter User's Account Type (Savings/Current): ").capitalize()
                    admin.create_account(name, email, address, account_type)
                elif admin_menu == "2":
                    account_number = int(input("Enter User's Account Number to delete: "))
                    admin.delete_user_account(account_number)
                elif admin_menu == "3":
                    toggle_option = input("Toggle Loan Feature On/Off (True/False): ")
                    admin.toggle_loan_feature(toggle_option.lower() == 'true')
                elif admin_menu == "4":
                    admin.view_user_accounts()
                elif admin_menu == "5":
                    print("Total Balance: $", admin.check_total_balance())
                elif admin_menu == "6":
                    print("Total Loan Amount: $", admin.check_total_loan_amount())
                elif admin_menu == "7":
                    toggle_option = input("Toggle Bankrupt Status On/Off (True/False): ")
                    admin.toggle_bankrupt_status(toggle_option.lower() == 'true')
                elif admin_menu == "8":
                    print("Admin Logout Successful.")
                else:
                    print("Invalid Admin Menu Option.")
            else:
                print("Invalid Admin Login.")
        else:
            print('Invalid Choice\n')
    else:
        print(f'\nWelcome {current_user.name}!\n')

        if current_user.account_type == 'Savings':
            print('1. Show Info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Apply Interest')
            print('5. Change Info')
            print('6. Show Transaction History')
            print('7. Take Loan')
            print('8. Transfer Money')
            print('9. Check Balance')
            print('10. Logout')

            op = input('Choose Option: ')

            if op == '1':
                print(f'Name: {current_user.name}')
                print(f'Account Number: {current_user.account_number}')
                print(f'Account Type: {current_user.account_type}')
                print(f'Balance: {current_user.balance}')
            elif op == '2':
                amount = float(input('Amount: '))
                current_user.deposit(amount)
            elif op == '3':
                amount = float(input('Amount: '))
                current_user.withdraw(amount)
            elif op == '4':
                interest_rate = float(input('Interest Rate (%): '))
                interest = (interest_rate / 100) * current_user.balance
                current_user.deposit(interest)
                print(f'Interest Applied: ${interest}')
            elif op == '5':
                name = input('New Name: ')
                email = input('New Email: ')
                address = input('New Address: ')
                account_type = input('New Account Type (Savings/Current): ').capitalize()
                current_user.name = name
                current_user.email = email
                current_user.address = address
                current_user.account_type = account_type
            elif op == '6':
                print('Transaction History:')
                for transaction in current_user.transaction_history:
                    print(transaction)
            elif op == '7':
                if current_user.loan_count > 0:
                    loan_amount = float(input('Loan Amount: '))
                    current_user.take_loan(loan_amount)
            elif op == '8':
                recipient_account = int(input('Recipient Account Number: '))
                recipient = User.user_exists(recipient_account)
                if recipient is None:
                    print('Recipient account does not exist.')
                else:
                    transfer_amount = float(input('Amount to Transfer: '))
                    current_user.transfer(recipient, transfer_amount)
            elif op == '9':
                print(f'Available Balance: {current_user.check_balance()}')
            elif op == '10':
                current_user = None
                print('\nLogout Successful\n')
            else:
                print('Invalid option.')
        elif current_user.account_type == 'Current':
            print('1. Show Info')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Change Info')
            print('5. Show Transaction History')
            print('6. Logout')

            op = input('Choose Option: ')

            if op == '1':
                print(f'Name: {current_user.name}')
                print(f'Account Number: {current_user.account_number}')
                print(f'Account Type: {current_user.account_type}')
                print(f'Balance: {current_user.balance}')
            elif op == '2':
                amount = float(input('Amount: '))
                current_user.deposit(amount)
            elif op == '3':
                amount = float(input('Amount: '))
                current_user.withdraw(amount)
            elif op == '4':
                name = input('New Name: ')
                email = input('New Email: ')
                address = input('New Address: ')
                account_type = input('New Account Type (Savings/Current): ').capitalize()
                current_user.name = name
                current_user.email = email
                current_user.address = address
                current_user.account_type = account_type
            elif op == '5':
                print('Transaction History:')
                for transaction in current_user.transaction_history:
                    print(transaction)
            elif op == '6':
                current_user = None
                print('\nLogout Successful\n')
            else:
                print('Invalid option.')
