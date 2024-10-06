import pandas
import mysql.connector
import smtplib
import random
import time
# import csv

# dadabase connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123"
)

mydb = db.cursor()

# common_database = mydb.execute("create database common_database")
mydb.execute("use common_database")
# emp_table = ("create table all_employee (adid varchar(20), f_name varchar(20), l_name varchar(20), "
#              "emp_email varchar(40), location varchar(20))")
# mydb.execute(emp_table)

with open("allemployee.csv",) as emp_data:
    reader = pandas.read_csv("allemployee.csv")


with open("cab_details.csv") as cab:
    cabreader = pandas.read_csv("cab_details.csv")


def mail():
    sender_mail = "faltuuseless215@gmail.com"
    receiver_mail = trip['emp_mail']
    # print(receiver_mail)
    # receiver_mail = trip['emp_mail']
    subject = "Trip Details"
    message = f"Your trip will start soon\n\nsign-in otp{inotp}\nsign-out otp{outotp}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    text = f"Subject: {subject},\n\n{message}"
    server.login(sender_mail, "asvjvmsvdpywitkk")
    server.sendmail(sender_mail, receiver_mail, text)
    print(f"Message has been sent")

def no_show():
    sender_mail = "faltuuseless215@gmail.com"
    receiver_mail = trip['emp_mail']
    # print(receiver_mail)
    receiver_mail = trip['emp_mail']
    subject1 = "No-Show"
    message1 = "You have been marked as a No-Show"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_mail, "asvjvmsvdpywitkk")
    text1 = f"Subject: {subject1},\n\n{message1}"
    server.sendmail(sender_mail, receiver_mail, text1)
    print(f"Message has been sent")
    text1 = f"Subject: {subject1},\n\n{message1}"

duration = 10
stop_duration = 0
count = 5
# emp_present = ""




for index,trip in reader.iterrows():
    # print(trip["trip"])
    if trip['trip_status'] == "yes":
        trip_name = trip['fname']
        print(trip_name)
        inotp = random.randint(1000, 9999)
        outotp = random.randint(1000, 9999)
        print(inotp)
        print(outotp)
        # mail()
        driver = input("Driver Enter journey status\t\t").lower()
        if driver == "waiting":
            j = int(input(f"{trip["fname"]}\tenter your sign-in otp   ")) or input("Enter absent if employee not available").lower()
            if inotp != j:
                while inotp != j:
                    # if inotp == j:
                        print(input(f" you have entered incorrect otp\t\t"))
                        # if trip['trip_status'] == "no":
                        count -= 1
            elif inotp == j or j == "absent":
                pass

out = outotp
# print(out)

driver = input("Driver Enter journey status\t\t").lower()
if driver == "start":
    print("Trip Started")
    for i in range(int(duration)):
        # print(duration)
        duration = duration - 1
        time.sleep(1)
        print(duration)

count = 10
for index, trip in reader.iterrows():
    # print(out)
    if trip['trip_status'] == "yes":
        print(out)
        out_otp = int(input(f"{trip["fname"]}   enter your sign-out otp   "))
        while out != out_otp:
            # print("final")
            # print(out)
            if out == out_otp:
                print(input(f" you have entered incorrect otp\t\t"))
            else:
                print("enter correct otp")
                count += 1
                # print(out)




# driver = input("Driver Enter journey status\t\t").lower()
# if driver == "start":
#     print("Trip Started")
#     for i in range(int(duration)):
#         # print(duration)
#         duration = duration - 1
#         time.sleep(1)
#         print(duration)

#
# for index, trip in reader.iterrows():
#     if trip['trip_status'] == "yes":
#         out_otp = int(input(f"{trip["fname"]}   enter your sign-out otp   "))
#         while outotp != out_otp:
#             if outotp == out_otp:
#                 print(input(f" you have entered incorrect otp\t\t"))
#             else:
#                 print("enter correct otp")
#                 count += 1

print("trip completed")






