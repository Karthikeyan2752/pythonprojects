#importing date and time and mysql.connector fpr database connection

from datetime import datetime
import mysql.connector

#this code prints the date in correct format

now=datetime.now()
dateTime=now.strftime("%d/%m/%y %H:%M:%S")

#assigning user details in tuples

userName = ["ramkumar", "abdulkalam", "ramesh", "ravanan", "karthikeyan"]
pinCode = ["2233", "1999", "2424", "1985", "5555"] 
accountNumber = ['22131353', '22199281', "22182838", "22185597", "22667432"]
balance = [98888, 56777, 6741871, 279638, 91820]

#this functions will print the available denominations

def denominations():
    print("AVAILABLE DENOMINATIONS")
    print("500s|2000s|200s|100s")

#using flag , this will run loop until we declare that flag=false
# giving flase as a default value for false
 
flag = False
#this for loop will run 999 times ,people can use this atm 999 times
for i in range (0,999): 
    print("********************************************************************")
    print("\t\WELCOME TO STATE BANK OF INDIA ATM")
    print("********************************************************************")
    print(f"date and time :{dateTime} ")
    inputName = input("Enter Your Name: ")

#converting the input name into lower case,so the name is not case sensitive

    inputName = inputName.lower()

#assigning 0000 as a default value  for pin    
#assigning 0 as a default value  for indexvalue of pin and name 
   
    inputPin = 0000 
    index = 0

#this for loop will check input name with name in list and get index no. of name 
#    
    for name in userName:
        count = 0
        if name == inputName:
            index = count 
            #index of name is stored
            inputPin = input("ENTER THE 4 DIGIT PIN: ")
        count += 1#count=count+1

#this  if statement will check the index of pin corresponding to name with the pin that user entered is same   
       
    if inputPin == pinCode[index]:
        flag = True
    else:
        print("Invalid data.")
#if the index does not match flag=flase will stop the loop
        flag = False
#continue will continue the loop        
        continue
#if the pin indexes matches if statement will assign flag=true and print the options available    
    if flag == True:
        tempPin=pinCode[index]
        print(f"\nYOUR ACCOUNT NUMBER IS: {accountNumber[index]}")
        print("PRESS 1 FOR DEPOSIT")
        print("PRESS 2 FOR WITHDRAWL")
        print("PRESS 3 FOR BALANCE ENQUIRY")
        print("PRESS 4 FOR CHANGING PIN")
        print("PRESS 5 FOR EXIT")

#getting the choice from the user (only int)
        choice = int(input("CHOOSE YOUR OPTION:"))

#this if statement is for withdrwal option

    if choice == 2:
        amount = input("\nEnter the amount you want to withdraw: ")

#this line of code will connect to sql database 
        #mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752")
        #mycursor.execute("create database sbiatmtransaction")
        mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752",database="sbiatmtransaction")

#this will create cursoor object        

        mycursor=mydb.cursor()

#this  will execute the sql query
        #CREATE TABLE atmUsersDetails (username varchar(30),pin int(4),balance int(10),dateAndtime varchar(30)); 
        #mycursor.execute("create table atmuserdetails(name varchar(30),dateandtime varchar(30),balance varchar(10))")       
        mycursor.execute("insert into atmuserdetails (name,dateandtime,balance) value(%s,%s,%s)" ,inputName,dateTime,remainingBalalnce)

#exception handling   
        try: 
            amount = int(amount)
            if amount > balance[index]:
#raise will stop the loop                
                raise
#if the try fails the except block will run 
        except:
            print("invalid amount.")
#continue statement continue to next   
#          
            continue
        remainingBalalnce = balance[index] - amount 
#remove method remove the old balance        
        balance.remove(balance[index]) 
#insert method insert the neww balance                
        balance.insert(index,remainingBalalnce)
        availableBalance = print(f"\nAVAILABLE BALANCE:{remainingBalalnce} ")
        
    elif choice == 1:
        amount = input("ENTER THE DEPOSITED AMOUNT: ")
        remainingBalalnce = balance[index] + amount 
        balance.remove(balance[index])
        #remove method remove the old balance 
        balance.insert(index,remainingBalalnce)
        #insert method insert the neww balance 
        availableBalance = print(f"Your available balance is: {remainingBalalnce}")

    elif choice == 3:
        print(f"Your account balance is: Rs.{balance[index]}" )

#this elif   statement will change the pin   
    
    elif choice == 4:
        oldpin = (input("ENTER THE OLD PIN:"))

#if the pin entered by user does not match the old pin in list , it goes to starting point
        if oldpin!=pinCode[index]:
            print("OLD PIN DOES NOT MATCH!!")
            print("TRY AGAIN!")

#if the pin matches              
        else:    
            print("1.PIN MUST CONTAIN ONLY FOUR DIGITS")
            print("2.PIN MUST NOT CONTAIN ANY OTHER SPECIAL CHARACTERS")
#getting the new pin they want to change

            newPin=(input("ENTER THE NEW PIN YOU WANT TO CHANGE:"))

#if old pin and new pin are same it will go to starting point   
    
            if newPin == oldpin:
                print("NEW PIN MUST NOT BE SAME AS OLD PIN")
            else:
#changing the old pin by assigning new pin

                pinCode[index]= newPin
                print("PIN CHANGED SUCCESSFULLY!")  
                
    print("THANK YOU FOR USING STATE BANK OF INDIA ATM")
    print("VISIT AGAIN")







