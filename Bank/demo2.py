class Account:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")

    def check_balance(self):
        return self.balance

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.transaction_history.append(f"Took a loan of {amount}")
        else:
            print("Loan limit exceeded")

    def get_transaction_history(self):
        return self.transaction_history


class User(Account):
    def __init__(self, name, email, address, account_type, account_number):
        super().__init__(name, email, address, account_type, account_number)


class Admin(Account):
    def __init__(self, username, password):
        super().__init__(None, None, None, None, None)
        self.username = username
        self.password = password


class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.loan_feature_enabled = True
        self.total_balance = 0
        self.total_loan_amount = 0

    def create_user_account(self, name, email, address, account_type):
        account_number = len(self.users) + 1
        user = User(name, email, address, account_type, account_number)
        self.users.append(user)
        return user

    def delete_user_account(self, user):
        self.users.remove(user)

    def get_user_accounts(self):
        return self.users

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

    def deposit_amount(self, user, amount):
        user.deposit(amount)
        self.total_balance += amount

    def withdraw_amount(self, user, amount):
        if user.check_balance() >= amount:
            user.withdraw(amount)
            self.total_balance -= amount
        else:
            print("Withdrawal amount exceeded")

    def transfer_amount(self, user, recipient_account_number, amount):
        recipient = self.get_user_by_account_number(recipient_account_number)
        if recipient:
            if user.check_balance() >= amount:
                user.withdraw(amount)
                recipient.deposit(amount)
            else:
                print("Insufficient balance")
        else:
            print("Account does not exist")

    def get_user_by_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

    def create_admin_account(self, username, password):
        admin = Admin(username, password)
        self.admins.append(admin)
        return admin

    def get_admin_by_username(self, username):
        for admin in self.admins:
            if admin.username == username:
                return admin
        return None


class ReplicaSystem:
    def __init__(self):
        self.bank = Bank()
        self.current_user = None
        self.admin_registered = False

    def user_register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account type: ")
        user = self.bank.create_user_account(name, email, address, account_type)
        print(f"User account created successfully. Account number: {user.account_number}")

    def admin_register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        admin = self.bank.create_admin_account(username, password)
        self.admin_registered = True
        print("Admin account created successfully.")

    def user_login(self):
        account_number = int(input("Enter your account number: "))
        user = self.bank.get_user_by_account_number(account_number)
        if user:
            self.current_user = user
            print("User logged in successfully.")
        else:
            print("Invalid account number. Please try again.")

    def admin_login(self):
        if not self.admin_registered:
            print("Admin account not registered. Please register first.")
            return

        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password == "admin":
            self.current_user = "admin"
            print("Admin logged in successfully.")
        else:
            print("Invalid username or password. Please try again.")

    def user_menu(self):
        while True:
            print(f"\nWelcome, {self.current_user.name}! What would you like to do? You can choose from the following options:")
            print("1. Deposit Amount")
            print("2. Withdraw Amount")
            print("3. Transfer Amount")
            print("4. Check Balance")
            print("5. Take Loan")
            print("6. View Transaction History")
            print("7. Logout")

            choice = input()

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                self.bank.deposit_amount(self.current_user, amount)
                print("Amount deposited successfully.")

            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                self.bank.withdraw_amount(self.current_user, amount)
                print("Amount withdrawn successfully.")

            elif choice == "3":
                recipient_account_number = int(input("Enter the recipient's account number: "))
                amount = float(input("Enter the amount to transfer: "))
                self.bank.transfer_amount(self.current_user, recipient_account_number, amount)
                print("Amount transferred successfully.")

            elif choice == "4":
                balance = self.current_user.check_balance()
                print(f"Your current balance is: {balance}")

            elif choice == "5":
                if self.bank.loan_feature_enabled:
                    amount = float(input("Enter the loan amount: "))
                    self.current_user.take_loan(amount)
                    print("Loan taken successfully.")
                else:
                    print("Loan feature is currently disabled.")

            elif choice == "6":
                transaction_history = self.current_user.get_transaction_history()
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)

            elif choice == "7":
                self.current_user = None
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def start(self):
        while True:
            print("\nWelcome to the Replica Banking System!")
            print("1. User Register")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Quit")

            choice = input("Select an option: ")

            if choice == "1":
                self.user_register()
            elif choice == "2":
                self.user_login()
                if self.current_user:
                    self.user_menu()
            elif choice == "3":
                self.admin_login()
                if self.current_user:
                    self.admin_menu()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View User Accounts")
            print("2. View Total Balance")
            print("3. View Total Loan Amount")
            print("4. Enable Loan Feature")
            print("5. Disable Loan Feature")
            print("6. Logout")

            choice = input("Select an option: ")

            if choice == "1":
                user_accounts = self.bank.get_user_accounts()
                print("User Accounts:")
                for user in user_accounts:
                    print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}")

            elif choice == "2":
                total_balance = self.bank.get_total_balance()
                print(f"The total balance in the bank is: {total_balance}")

            elif choice == "3":
                total_loan_amount = self.bank.get_total_loan_amount()
                print(f"The total loan amount in the bank is: {total_loan_amount}")

            elif choice == "4":
                self.bank.enable_loan_feature()
                print("Loan feature enabled.")

            elif choice == "5":
                self.bank.disable_loan_feature()
                print("Loan feature disabled.")

            elif choice == "6":
                self.current_user = None
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please select a valid option.")
    
    def start(self):
        while True:
            print("Welcome to the Replica Banking System!")
            print("1. User Register")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Quit")

            option = input("Select an option: ")

            if option == "1":
                self.user_register()
            elif option == "2":
                self.user_login()
            elif option == "3":
                self.admin_login()
            elif option == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


system = ReplicaSystem()
system.start()