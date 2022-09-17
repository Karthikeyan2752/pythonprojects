#importing date and time and mysql.connector for database connection

from datetime import datetime
import mysql.connector

#this code prints the date in correct format

now=datetime.now()
dateTime=now.strftime("%d/%m/%y %H:%M:%S")

print("!!!!!!!!!!WELCOME TO BOOKMYTICKET.COM!!!!!!!!!!")
print("\tyour perfect ticket booking partner....")
print(dateTime)
#getting the location from the user
location = input("ENTER YOUR LOCATION:")

#this screenselection() function prints the available screens

def screenselection():
    print("*****AVAILABLE SCREENS*****")
    print("1. SILVER")
    print("2. PEARL")
    print("3. DIAMOND")    

#this seats() function prints the available seats             

def seats():
    print("AVAILABLE SEATS")
    print("A1,A2,A3,A4,A5.......A25")
    print("B1,B2,B3.............B25")
    print(".")
    print(".")
    print(".")
    print("Z1,Z2................Z25")

#this payment() function prints the available MODE OF PAYMENT    
                
def payment():

    print("AVAILABLE MODE OF PAYMENT")
    print("1.UPI")
    print("2.NEFT")
    print("3.CARD")

#this function prints the upi id and bank details 

def modeofp():
    if pay == 1:
        mode="UPI"
        print("UPI ID:bookmytickets@oksbi")
    elif pay ==2:
        mode="NEFT" 
        print("IFSC:SBI27272,BRANCK:KODAMBAKKKAM,ACCOUNT NUMBER:22733384,BANK:SBI")
    elif pay == 3:
        mode="CARD"
    else:
        print("INVALID INPUT!")

#the upcoming four functions prints the theatres available in cities        

def chennai():
    print("*****THEATRES IN CHENNAI*****")
    print("ROHINI SILVER SCREENS - KOYAMBEDU")
    print("KASI TALKIES - KK NAGAR")
    print("KAMALA THEATRE - VADAPALANI")
    print("AGS CINEMAS - MADURAVOYAL")
    print("PVR CINNEMAS - ANNA NAGAR")

def madurai():
    print("*****THEATRES IN MADURAI*****")
    print("VIMALA CINEMAS - ANNA NAGAR")
    print("RANESH TALKIES - THIRUMANGALAM")
    print("MAHESH THEATRE - ILANGO NAGAR")
    print("KASI TALKIES - MATUTHAVANI")

def kovai():
    print("*****THEATRES IN KOVAI*****")
    print("SHYMALA CINEMAS - INDIRA NAGAR")
    print("RANVEER TALKIES - BABA NAGAR")
    print("MAHESHBABU THEATRE - POLLACHI")
    print("KASI TALKIES - GANDHI NAGAR")

def trichy():
    print("*****THEATRES IN TRICHY*****")
    print("SURESH CINEMAS - LAKSHI NAGAR")
    print("MEGA TALKIES - ASTALAKSHMI NAGAR")
    print("SAM THEATRE - THIRUVIDANTHAI")
    print("INOX CINEMAS - INTUC NAGAR")

def nellai():
    print("*****THEATRES IN NELLAI*****")    
    print("GANESH CINEMAS - GANAPATY NAGAR")
    print("KAPOOR TALKIES -  MC NAGAR")
    print("SURIYAN THEATRE - KUTRALAM")
    print("PANNEER TALKIES - NETAJI NAGAR")

# this if elif else statement check the location and prints the theatres available in that location

if location=="chennai":
    chennai()
elif location=="madurai":
    madurai()
elif location=="trichy":
    trichy()
elif location=="kovai":
    kovai()
elif location=="nellai":
    nellai()
else:
    print("SORRY OUR SERVICE IS ONLY AVAILABLE IN\n@CHENNAI\n@MADURAI\n@KOVAI\n@TRICHY\n@NELLAI")
    quit()

#coming 6 lines of code get details from the user

theatre = input("ENTER THE THEATRE NAME YOU WANT:")
firstName=input("ENTER YOUR FIRST NAME:")
lastName=input("ENTER YOUR LAST NAME:")
name=lastName+firstName
mobile=input("ENTER YOUR MOBILE NUMBER:")
emailId=input("ENTER YOUR EMAIL ID:")
#calling the method
screenselection()

screen = input("ENTER THE SCREEN NAME:")
times={1:"10.00 AM -  1.00 PM",2:"2.00 PM - 5.00 PM",3:"6.00 PM - 9.00 PM",4:"10.00 PM -1.00 AM"}
print(times)

timing=int(input("ENTER YOUR TIMING:"))

#this codes will print the screen and that time user have chosen

if timing==1:
    print(f"YOUR HAVE CHOSEN {screen} AT {times[1]}")
elif timing==2:
    print(f"YOUR HAVE CHOSEN {screen} AT {times[2]}")
elif timing == 3:
    print(f"YOUR HAVE CHOSEN {screen} AT {times[3]}")
elif timing==4:
    print(f"YOUR HAVE CHOSEN {screen} AT {times[4]}")
else:
    print("INVALID INPUT")
#calling the method
seats()

seatno=input("ENTER YOUR SEAT NAME(EG. A1,A2,A3. PERIODS AND COMMA ARE NECESSARY):")
b=len(seatno)
tickets=b/3
print(f"TOTAL NUMBER OF TICKETS:{tickets}")

#giving sepaprate ticket prices based on screens ,this code will calculate the total amount

if screen=="pearl":
    totalamount=tickets*120
elif screen == "silver":
    totalamount=tickets*80
elif screen == "diamond":
    totalamount=tickets*180    
else:
    print("INAVLID INPUT!")
#calling the method
payment()

pay=int(input("SELECT MODE OF PAYMENT 1/2/3:"))
#calling the method
modeofp()

#this codes  will print the tickets

print("BOOKING SUCCESFULL, HAVE YOUR TICKET!")
print(dateTime)
print(f"NAME: {name}")    
print(f"MOBILLE: {mobile}") 
print(f"EMAIL ID: {emailId}") 
print(f"THEATRE: {theatre}") 
print(f"SCREEN: {screen}") 
print(f"TOTAL NUMBER OF TICKETS: {tickets}") 
print(f"TOTAL AMOUNT PAID: {totalamount}") 

#connecting to the server
mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752")

#code for databse and table creation
#create database if not exists bookmytickets;
#create table if not exists details(name varchar(30),mobile_number varchar(13),email varchar(30),location varchar(30),theatre varchar(30),nooftickets varchar(3),screen varchar(6));

#connecting to the table
mydb=mysql.connector.connect(host="localhost",user="root",password="Karthikn2752",database="bookmytickets")
#creating cursor object
mycursor=mydb.cursor()
#executing the MySQL command
mycursor.execute("INSERT INTO details (name,mobile_number,email,location,theatre,nooftickets,screen) values (%s,%s,%s,%s,%s,%s,%s)", (name,mobile,emailId,location,theatre,tickets,screen))
#commit the changes to  database
mydb.commit()
                










