import pickle
import os
import pathlib


class Account:
    AccountNumber = 0
    Name = ''
    Deposit = 0
    type = ''

    def createNewAccount(self):
        self.AccountNumber = int(input("Enter the account number : "))
        self.Name = input("Enter the Account Holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.Deposit = int(input("Enter The Initial amount(>=1000 for Saving and >=2000 for current"))
        print("\n\n\nNew Account Created")

    def DisplayAccount(self):
        print("Account Number : ", self.AccountNumber)
        print("Account Holder Name : ", self.Name)
        print("Type of Account", self.type)
        print("Balance : ", self.Deposit)

    def EditAccount(self):
        print("Account Number : ", self.AccountNumber)
        self.Name = input("Edit Account Holder Name :")
        self.type = input("Edit type of Account :")
        self.Deposit = int(input("Edit Balance :"))


    def getAcccountHolderName(self):
        return self.Name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.Deposit


def Introduction():
    print("\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$")
    print("\t\t\t\tWELCOME TO BANK")
    print("\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$")

    print("\t\t\t\tPRESENTED BY :")
    print("\t\t\t\tBANKOFINDIA")
    input()


def WriteAccount():
    account = Account()
    account.createNewAccount()
    writeAccountsFile(account)


def DisplayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.AccountNumber, " ", item.Name, " ", item.type, " ", item.Deposit)
        infile.close()
    else:
        print("NO ENTRY TO DISPLAY")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.AccountNumber == num:
                print(" Account Balance is = ", item.Deposit)
                found = True
    else:
        print("No Entry to Find")
    if not found:
        print("No existing Entry with this Number")


def AmountDepositAndAmountWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.AccountNumber == num1:
                if num2 == 1:
                    amount = int(input("Enter the Amount to Deposit : "))
                    item.Deposit += amount
                    print("Your Account is Updted")
                elif num2 == 2:
                    amount = int(input("Enter the Amount to Withdraw : "))
                    if amount <= item.Deposit:
                        item.Deposit -= amount
                        print("Available Balance is",item.Deposit)
                    else:
                        print("You cannot withdraw larger amount")

    else:
        print("No Entry to Find")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def DeactivateAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.AccountNumber != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def EditAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.AccountNumber == num:
                item.Name = input("Enter the Account Holder Name : ")
                item.type = input("Enter the Account Type : ")
                item.Deposit = int(input("Enter the Amount to Deposit : "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


# start of the program
ch = ''
num = 0
Introduction()

while ch != 8:
    # system("cls");
    print("\tWELCOME")
    print("\t1.  CREATE NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. VIEW BALANCE ")
    print("\t5. LIST OF ALL ACCOUNT HOLDERS ")
    print("\t6. DELETE AN ACCOUNT")
    print("\t7. EDIT AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()
    # system("cls");

    if ch == '1':
        WriteAccount()
    elif ch == '2':
        num = int(input("\tEnter The account Number. : "))
        AmountDepositAndAmountWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        AmountDepositAndAmountWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        DisplayAll();
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        DeactivateAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        EditAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else:
        print("Invalid choice")

    ch = input("Enter your choice : ")