from datetime import datetime
import mysql.connector

#this code will connect to the database

"""
mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752")
mycusor.execute(create database if not exists hotelITC)
"""
#this code prints the date in correct format

now=datetime.now()
dateTime=now.strftime("%d/%m/%y %H:%M:%S")

print("$$$$$$$$$ WELCOME TO HOTEL ITC GUINDY $$$$$$$$$")
print(dateTime)
print("ENTER 1 FOR BOOKING DETAILS AND REQUIREMETS")
print("ENTER 2 FOR ROOM BOOKING")
print("ENTER 3 FOR HALL BOOKING")
print("ENTER 4 FOR AVAILABLE SERVICES")
print("ENTER 5 FOR CHECKING THE DETAILS")
print("ENTER 6 FOR FOOD")
print("ENTER 7 FOR EXIT")

#this method will display the details entered by user

def displayDetails():
    print(f"NAME:{custName}")
    print(f"ADDRESS:{custAddress}")
    print(f"ID PROOF:{custIdProofNum}")
    print(f"MOBILE NUMBER:{custPhoneNo}")
    print(f"ALTERNATIVE NUMBER:{custAltNum}")
    print(f"CHECK IN DATE AND TIME{checkIn}")
    print(f"CHECK OUT DATE AND TIME{checkOut}")

#this method will display the requirements for booking

def bookingDetails():
    print("****REQUIREMENTS FOR BOOKINNG****")
    print("1.ID PROOF ISSUED BY GOVERNMENT")
    print("2.PERMANENT RESIDENTIAL ADDRESS")
    print("3.ADVANCE PAYMENT OF RS.2000(NON REFUNDABLE)")

#this method will let the user to book the rooms

def roomBooking():
    print("*****AVAILABLE TYPE OF ROOMS*****") 
#assignin room prices      
    normal=3000
    premium=4000
    elite=6000
    print("ENTER 1 FOR NORMAL")
    print("INR 3000 PER DAY normal:AC/DOUBLE BED/TV")
    print("MAXIMUM PERSONS ALLOWED:2")
    print("ENTER 2 FOR PREMIUM")
    print("INR 4000 PER DAY premium:AC/RELAX AREA/TV/BATH TUB/TV")
    print("MAXIMUM PERSONS ALLOWED:3")
    print("ENTER 3 FOR ELITE")  
    print("INR 6000 PER DAY elite:AC/RELAX AREA/TV/BATH TUB/BIG SCREEN TV/SMOKING AREA/CUSTOMISED THEME")
    print("MAXIMUM PERSONS ALLOWED:5")

  #getting the choice and no. of days from the user

    choice=int(input("ENTER YOUR ROOM TYPE:"))
    howManydays=int(input("ENTER THE NUMBER OF DAYS YOUR WANT TO STAY:"))
#calculating the amount and assigning it to new variables

    norm=normal*howManydays
    pre=premium*howManydays
    el=elite*howManydays

#printing the amounts based on choice    
    if choice==1:
        print("YOU HAVE CHOSEN NORMAL")
        print(f"TOTAL AMOUNT FOR ROOM IS:{norm} ")
    elif choice ==2:
        print("YOU HAVE CHOSEN PREMIUM")
        print(f"TOTAL AMOUNT FOR ROOM IS:{pre} ")
    elif choice==3:
        print("YOU HAVE CHOSEN ELITE")
        print(f"TOTAL AMOUNT FOR ROOM IS: {el}")
    else:
        print("INVALID CHOICE") 

#this method will let the user to book party hall        

def hallBooking():
    print("*****AVAILABLE HALLS*****")    
    print("ENTER 1 FOR CONFERENCE HALL(ONLY FOR OFFICIAL PURPOSES)")
    hallRent1=50000
    hallRent2=200000
    hallRent3=59000
    print("ENTER 2 FOR 500 SEATER PARTY HALL")
    print("ENTER 3 FOR 100 SEATER PARTY HALL")   

    choice2=int(input("ENTER THE TYPE OF OF HALL:") )
    howManydays2=input("ENTER THE NUMBER OF DAYS YOUR WANT TO RENT:")

    if choice2==1:
        print("YOU HAVE CHOSEN CONFERENCE HALL")
        print("TOTAL AMOUNT FOR ROOM IS: ",hallRent1*howManydays2)
    elif choice2==2:
        print("YOU HAVE CHOSEN 500 SEATER PARTY HALL")  
        print("TOTAL AMOUNT FOR HALL RENT IS: ",hallRent2*howManydays2)  
    elif choice2==3:
        print("YOU HAVE CHOSEN 100 SEATER PARTY HALL")
        print("TOTAL AMOUNT FOR HALL RENT IS: ",hallRent3*howManydays2)
    else:
        print("INVALLID CHOICE")

#this method will print the available services in the hotel

def availServices():
    print("*****AVAILABLE SERVICES*****")
    print("1.SWIMMING POOL")
    print("2.MASSAGE CENTER")
    print("3.UNISEX SPA AND SALOON")
    print("4.CHILDRENS PLAY AREA")
    print("5.MEN AND WOMEN PLAY AREA")
    print("6.PUB AND LIQUOR SHOP")

#this method will the let the user to choose the food and display the prices

def food():
    print("*****24 X 7 AVAILABLE FOODS*****")
    print("ENTER 1 FOR INDIAN FOODS")
    print("ENTER 2 FOR AMERICAN FOODS")
    print("ENTER 3 FOR ITALIAN FOODS")
    print("ENTER 4 FOR BEVARAGES")

    choice3=int(input("ENTER YOUR CHOICE:"))

    if choice3==1:
        print("1.DOSA==>200\n2.BRIYANI==>500\nCHICKEN GRILL==>700\n3.INDIAN SPECIAL SAMBAR RICE==>500\n4.NAAN & PANNEER BUTTER MASALA==>400")
    elif choice3==2:
        print("1.CHEESE BURGER==>250\n2.NACHOAS==>300\n2.OTDOGS==>300")
    elif choice3==3:
        print("CHEESEPIZZAS==>600\nPEPRONI PIZZA==>1000\nCHICKEN PIZZA==>1200")
    elif choice3==4:
        print("COFFEE==>100\nAPPLE JUICE==>180\nCOLD COFFEE==>200")
    else:
        print("INVALID INPUT")

#main code here we call the methods  
# getting the choice from the user    

choice5=int(input("ENTER YOUR CHOICE:"))

if choice5==1:
    bookingDetails()

#this elif statement will get the details from the user and go for roomboooking method

elif choice5==2:
    custFirstName=input("ENTER YOUR FIRST NAME:")
    custlastName=input("ENTER YOUR LAST NAME:")
    custName=custlastName+custFirstName
    custIdProofNum=input("ENTER YOUR ID NUMBER(AADHAAR,DRIVING LISCENSE ONLY):")
    custPhoneNo=input("ENTER YOUR MOBILE NUMBER:")
    custAltNum=input("ENTER YOUR ALTERNATIVE MOBILE NUMBER:")
    custAddress=input("ENTER YOUR ADDRESS:")
    checkIn=input("ENTER THE CHECKIN DATE AND TIME(IN DD/MM/YYYY,HH:MM:SS FORMAT)")
    checkOut=input("ENTER THE CHECKOUT DATE AND TIME(IN DD/MM/YYYY,HH:MM:SS FORMAT)")
    roomBooking()

#this code will connect to the databse and table

    """mycursor.execute("create table if not exists customerDetails(name varchar(30),IDproof varchar(30),phonenumber varchar(10),altnumber varchar(10),address varchar(255),checkin varchar(30),checkout varchar (30))")"""
    mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752",database="hotelITC")
    mycursor=mydb.cursor()
#this code will save the user data into database

    mycursor.execute("INSERT INTO customerdetails (name,IDproof,phonenumber,altnumber,address,checkin,checkout) values(%s,%s,%s,%s,%s,%s,%s)", (custName,custIdProofNum,custPhoneNo,custAltNum,custAddress,checkIn,checkOut))
    mydb.commit()

elif choice5==3:
#this elif statement will get the details from the user for hall booking

    custFirstName=input("ENTER YOUR FIRST NAME:")
    custlastName=input("ENTER YOUR LAST NAME:")
    custName=custlastName+custFirstName
    custIdProofNum=input("ENTER YOUR ID NUMBER(AADHAAR,DRIVING LISCENSE ONLY):")
    custPhoneNo=input("ENTER YOUR MOBILE NUMBER:")
    custAltNum=input("ENTER YOUR ALTERNATIVE MOBILE NUMBER:")
    custAddress=input("ENTER YOUR ADDRESS:")
    hallBooking()

#coming elif statements displays the corresponding details    
elif choice5==4:
    availServices()
elif choice5==5:
    displayDetails()
elif choice5==6:
    food()
elif choice5==7:

#quit function will quit the program
    quit()
else:
    print("INVALID CHOICE")

print("THANK YOU VISIT AGAIN!")

