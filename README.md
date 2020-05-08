# snbank
##### Banking System with FileSystem: login, create account and check account

This is a simple Banking system which reads Files to confirm staff authorization to the bank data (customer.txt file) and retrive the customers details.

## Usage

**NOTE**: Ensure you have the customer.txt and the staff.txt file in the same directory as the snBank.py.

Open the snBank.py code... run it
On running the code, a welcome oage is displayed

WELCOME PAGE looks like this:
```
      Welcome to snBank
        1 Staff login
        2 Close app
 ```

you need a valid staff login to access the STAFF LOGIN page
Open the staff.txt file and copy the username and password of any staff available in the file.

Choose "1" then Supply the USERNAME AND PASSWORD when prompted.

A banking option is displayed...

```
        STAFF LOGIN PAGE
    1 Create new bank account
    2 Check Account Details
    3 Logout
```

From the above options, Choose a number corresponding to what you'll like to do

```
    "1" To create an account.Supply the details to the promptsMakes sure to follow save the generated account number ^_^.This is to allow you retrieve your account details (Option 2).

    "2" To check registered accounts, do so by simply supplying your account number to the prompt.
    You get all your reistered details.

    "3" To logout from your current login session and back to the staff login page.
```

if "3" was chosen to LOGOUT, you get sent back to the Welcome page.
On the welcome page
```
      Welcome to snBank
        1 Staff login
        2 Close app
 ```

 Choosing "2" will terminate the code. 
 To access again to test other features, you need to RE-RUN the code.
