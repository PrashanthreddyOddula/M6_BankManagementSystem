# REQUIREMENTS
## Introduction
- Bank Management system : With this project, user can perform banking activities like in real bank. This perticular file contains all the details of requirement collection from user end.i.e, user can request performances like Account creation, Deposit,Withdraw,Balance enquiry,Etc.

# SWOT Analysis
![llllllllllllllllllllllllllllllllll](https://user-images.githubusercontent.com/46950972/161193339-2a465f0d-ceb8-4571-8aca-202abe91de63.png)


# 4W's and 1H
## Who:
- Everyone can use the bank management system who want to have benifit of banking.
## What:
- Bank management sysem is mainly concerned to Cover the major Banking activities in sigle application.
## When:
- User can use whenever he wants to access Bank services.
## Where:
- User can can access this application using any C compiler.
## How:
- Implementation is done using C language. And also used multifile concept.

# Detail requirement
## High level requirements
| SLno | Description |
| --- | --- |
| HLR1 |System Shall be able to open new Account | 
| HLR2 | User shall Deposit Money | 
| HLR3 | User shall Withdraw Money |
| HLR4 | User shall View Details | 
 
## Low level requirements 
| SLno | Description | 
| --- | --- | 
|LLR1	|To open new account user should provide name, type of account, initial Deposit|
|LLR2	|To Deposit Money User should provide Account number|
|LLR3	|To Withdraw Money User Should provide Account Number|
|LLR4	|To View Details User Should provide Account Number|
   

# TEST PLAN:

| *Test ID* | *Description*                                              | *Exp I/P* | *Exp O/P* |    
|-------------|--------------------------------------------------------------|------------|-------------|
|  T1       |Creation of new account| Name:abc , Account Number:6548655675,Account Type:C/S,Initia Deposit:2000 | Congratulations... Your account has been created.|
|  T2       |Deposit Amount|2000 |Your current available bank balance is 2000|
|  T3       |withdraw Amount|5000| Sorry, You dont have enough money in your account| 
|  T4       |Deactivate Account| Account Number |Account Deactivate|
|  T5       |Edit Account| Account Number |Account Updated|
|  T6       |If wrong choice chosen | 9 | Invalid choice |

# CONCLUSION
The Bank Management System is implemented for simplify the Users access towards bank function, I, e., like New Account Creation, Deposit, Withdraw, View Balance, Cancelation of Account, Editing the account. Therefor this Bank Management System is Built for All the Bank Services.
