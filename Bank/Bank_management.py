from abc import ABC,abstractmethod
class Account(ABC):
    accounts=[]

    def __init__(self,name,account_number,password,type) -> None:
        self.name=name
        self.account_number=account_number
        self.password=password
        self.type=type

        self.balance=0
        Account.accounts.append(self)

    def deposit(self,amount):
        if amount>=0:
            self.balance += amount
        else:
            print("\nInvaild Amount")

    def withdraw(self,amount):
        if amount>=0 and amount<=self.balance:
            self.balance -=amount
        else:
            print("\nInvaild Amount")

    def change_info(self,name):
        self.name=name

    def change_info(self,name,password):
        self.name=name
        self.password=password

    @abstractmethod
    def show_info(self):
        pass

class Savings_Account(Account):
    def __init__(self, name, account_number, password,interest_rate) -> None:
        super().__init__(name, account_number, password,'savings')
        self.interest_rate=interest_rate

    def show_info(self):
        print(f'\nInfos of Account {self.name}\n')
        print(f'\n Account Type: {self.type}')
        print(f'\n Account Number: {self.account_number}')
        print(f'\n Account Balance: {self.balance}')

    def apply_interest(self):
        interest=self.balance*(self.interest_rate/100)
        print(f'Applided interest of {interest}')
        self.deposit(interest)

class Special_Account(Account):
    def __init__(self, name, account_number, password,limit ) -> None:
        super().__init__(name, account_number, password, 'special')
        self.limit=limit
    
    def withdraw(self, amount):
        if amount>=0 and amount<=self.limit:
            self.balance -= amount
        else:
            print("\nInvaid Amount")

    def show_info(self):
        print(f'\nInfos {self.type} of Account {self.name}\n')
        print(f'\n Account Number: {self.account_number}')
        print(f'\n Account Balance: {self.balance}')

current_user=None
while(True):
    if current_user == None:
        print('\nNO User Login!\n')
        ch=input("\n Login or Register(L/R)")
        if ch=='R':
            name=input('Name:')
            no=input('Account Number: ')
            password=input("Password: ")
            a=input(('Saving or Special? (sv/sp)'))
            if a=='sv':
                interest_rate=int(input('Interest Rate: '))
                current_user=Savings_Account(name,no,password,interest_rate)
            elif a=='sp':
                limit=int(input('Overdraft Limit: '))
                current_user=Special_Account(name,no,password,limit)
            else:
                print('\nInvalid Choice\n')
        else:
            no=input('Account Number: ')
            for account in Account.accounts:
                if no == account.account_number:
                    current_user=account
                    break
    else:
        print(f'\nWelcome {current_user.name}!\n')

        if current_user.type=='savings':
            print('1.Showing info')
            print('2.Deposit')
            print('3.Withdraw')
            print('4.Apply Interest')
            print('5.Change Info')
            print('6.Logout')

            op=int(input('Choose Option:'))
            
            if op==1:
                current_user.show_info()
            elif op==2:
                amount=int(input('Amount:'))
                current_user.deposit(amount)
            elif op==3:
                amount=int(input('Amount:'))
                current_user.withdraw(amount)
            elif op==4:
                current_user.apply_interest()
            elif op==5:
                pass
            elif op==6:
                current_user=None
                print('\nLogout Successful\n')

        else:
            print('1.Showing info')
            print('2.Deposit')
            print('3.Withdraw')
            print('4.Change Info')
            print('5.Logout')

            op=int(input('Choose Option:'))
            
            if op==1:
                current_user.show_info()
            elif op==2:
                amount=int(input('Amount:'))
                current_user.deposit(amount)
            elif op==3:
                amount=int(input('Amount:'))
                current_user.withdraw(amount)
            elif op==4:
                pass
            elif op==5:
                current_user=None
                print('\nLogout Successful\n')