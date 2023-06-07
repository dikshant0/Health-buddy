#Health Buddy
import sys
import requests,re
import os
import random, csv
import pandas as pd

def mainMenu():
    #Calculating BMI
    #Generic drug information, and common diseases for an organ
    os.system("clear")
    print("\t\t\tWelcome to Health Buddy Menu")
    print("1. Calculate your Body Mass Index(BMI)")
    print("2. Get Generic drug name for a branded Medicine")
    print("3. Get drug information")
    print("4. Get common diseases for an organ")
    print("5. Log out")
    print("6. Exit")
    ch = int(input("Enter your Choice: "))
    match (ch):
        case 1:
            #BMI calculation
            API_KEY = "a0ab28982fmshe5938f0d17bcc74p16e788jsn679fa2036c2d"
            h = float(input("\nEnter your height(in meters): "))
            w = int(input("Enter your weight(in kilograms): "))
            #BMI formula rounded to 3 places
            bmi = round(float(w/(h*h)), 3)
            print("Your Body mass Index = ", bmi)
            if bmi < 18.5:
                print("You are Underweight")
            elif bmi > 18.5 and bmi <= 24.9:
                print("You are Normal weighted")
            elif bmi > 25.0 and bmi <= 29.9:
                print("You are Overweight")
            elif bmi > 30.0 and bmi <= 34.9:
                print("You are Obesity(class I)")
            elif bmi > 35.0 and bmi <= 39.9:
                print("You are Obesity(class II)")
            else:
                print("You fall under Extreme Obesity")

        case 2:
            #Generic Drug name for Branded medicine
            API_KEY = "a0ab28982fmshe5938f0d17bcc74p16e788jsn679fa2036c2d"
            drugName = input("Enter the name of the drug you want the Generic name of: ")
            url = "https://drug-info-and-price-history.p.rapidapi.com/1/genericname"
            querystring = {"drug": drugName}
            headers = {
                "X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
                }
            #API call using requests
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("The generic name of", drugName, "is", response.json()['generic_name'])
        case 3:
            #Description of Branded Medicine through API call
            API_KEY = "a0ab28982fmshe5938f0d17bcc74p16e788jsn679fa2036c2d"
            drugName = input("Enter the name of the drug you want information on: ")
            url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"
            querystring = {"drug": drugName}
            headers = {
                "X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(f"\n{drugName.upper()} INFORMATION\n")
            #Decription include Generic name, Strength of the medicine, Description, Manufacturer Name, Dosage and Form
            print(f"Generic Name: {response.json()[0]['active_ingredients'][0]['name']}")
            print(f"Strength: {response.json()[0]['active_ingredients'][0]['strength']}")
            print(f"Description: {response.json()[0]['packaging'][0]['description']}")
            print(f"Manufacturer Name: {response.json()[0]['openfda']['manufacturer_name'][0]}")
            print(f"Dosage, Form: {response.json()[0]['dosage_form']}")
        case 4:
            #Common Diseases associated with organs by API call
            API_KEY = "a0ab28982fmshe5938f0d17bcc74p16e788jsn679fa2036c2d"
            bodyPart = input("Enter the name of the body part: ")
            url = f"https://healthwise.p.rapidapi.com/body/diseases/%7B{bodyPart}%7D"
            headers = {
                "X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "healthwise.p.rapidapi.com"
                }
            response = requests.request("GET", url, headers=headers)
            print(response.text)

        case 5:
            #Log out of Health Buddy mainMenu
            main()
        case _:
            #Exiting the program
            print("Exiting!!")
            sys.exit(0)
    choice = input("Do you want to continue?(y/n): ").lower()
    if choice == "y" or choice =="yes":
        mainMenu()

def validate(username, password):
    #Validates the username and password from the file and returns True or False
    try:
        #checks the data csv file for username and password, if correct then login into Health Buddy mainMenu
        with open("data.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username and row["Password"] == password:
                    return True
                elif row["Username"] == username and row["Password"] != password:
                    print("Incorrect password!")
                    return False
            print("User Not Found, Please Sign-up")
            return False
    #if file doesn't exist
    except FileNotFoundError:
        print("No users detected")
        return False

def usernameValidator(username):
    #Checks whether the username if already taken by any other user
    while True:
        try:
            with open("data.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Username"] != username:
                        return False
            return True
        except FileNotFoundError:
            return False

def passwordValidator(password):
    #Check whether the password follows the prescribed guidelines
    #Password validation using Regular expression https://stackoverflow.com/questions/2990654/how-to-test-a-regex-password-in-python
    if re.fullmatch(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
        return True
    else:
        return False

def adminLoginValidator(a_uname, a_password):
    #Validates the login username and password
    admin_username = "Admin"
    admin_password = "Admin@1325"
    os.system("clear")

    if a_uname != admin_username:
        print("Wrong Username name!!")
        return False

    if a_password != admin_password:
        print("Wrong Password!!")
        return False
    else:
        return True

def adminMenu():
    #Allows the admin to See all registered users, see a specific user profile, and delete a user
    print("\tYou have signed in successfully\n\nHeres a list of things you can do:\n")
    print("1. See all user data")
    print("2. See a specific user profile")
    print("3. Delete a user")
    print("4. Log out")
    print("5. Exit")
    ch = int(input("Enter your Choice: "))
    match (ch):
        case 1:
            #open the data.csv file and print all the users data in a tabular format
            df = pd.read_csv("data.csv")
            print(df)
        case 2:
            #search a user by user name and show profile in table format
            find_username = input("Enter the username you want to find: ")
            flag = False
            with open("data.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Username"] == find_username:
                        flag = True
                        print(row)
            if flag == False:
                print("No user found")
        case 3:
            #delete a user by username
            delete_username = input("Enter the username you want to delete: ")
            flag = False
            list = []
            #Copying the content of the file into a list and then skipping the user to be deleted to be added in the list
            with open("data.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Username"] == delete_username:
                        flag = True
                    else:
                        list.append(row)
            if flag == False:
                print("No user found!")
            #Writing the list into the file again
            else:
                with open("data.csv", "w") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = ["Name", "Age", "Gender", "Username", "Password"])
                    writer.writeheader()
                    writer.writerows(list)
                    print(f"\nUser {delete_username} has been deleted.")
        case 4:
            #log out
            main()

        case _:
            #exiting the program
            sys.exit("Bye!")

    choice = input("Do you want to continue?(y/n): ").lower()
    if choice == "y" or choice =="yes":
        adminMenu()


def main():
    while True:
        try:
            os.system('clear')
            print("\n\t\t\t\tWelcome to Your Health Buddy\n")
            print("1. Existing User Login")
            print("2. New User - Sign Up")
            print("3. Admin Login")
            print("4. Exit")
            n = int(input("Enter your Choice Number: "))
            #Matching the menu as per the requirement
            match (n):
                case 1:
                    username = input("\nEnter Username : ")
                    password = input("\nEnter password : ")
                    if validate(username, password) == True:
                        #if login is successful call mainMenu(), ie the medical menu.
                        mainMenu()

                case 2:
                    os.system("clear")
                    print("\t\t\tWelcome to Sign-Up Menu")
                    name = input("\nEnter your Name: ")
                    age = int(input("Enter your Age: "))
                    gender = input("Enter your Gender(m/f): ").lower()
                    if(gender == "m"):
                        gender = "Male"
                    if(gender == "f"):
                        gender = "Female"
                    username = input("Enter your username: ")
                    if usernameValidator(username) == False:
                        print(f"\nCongratulations {username} is your username!")
                    else:
                        #if username is taken then new options are presented to the user
                        print("The username is already taken!")
                        print("\nSome available username are = ")
                        option1 = (username + str(random.randint(0, 333)))
                        option2 = (username + str(random.randint(334, 745)))
                        option3 = (username + str(random.randint(746, 999)))
                        print(f"\t{option1}\t{option2}\t{option3}")
                        username = input("Choose your username: ")
                        usernameValidator(username)

                    print("\n\t\tChoose a strong password")
                    print("\nThe password must contain: ")
                    print("Atleast 8 letters")
                    print("Atleast 1 Uppercase alphabet and 1 Lowercase alphabet")
                    print("Atleast 1 Digit and 1 Special symbol")
                    password = input("Choose a password : ")
                    if passwordValidator(password) == True:
                        #appending into the file
                        #checking if the file exists or not
                        if not os.path.exists("data.csv"):
                            #if the file does not exist then making a new file and writing the Headers
                            with open("data.csv", "w") as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames = ["Name", "Age", "Gender", "Username", "Password"])
                                writer.writeheader()
                                writer.writerow({"Name" : name, "Age": age, "Gender" : gender, "Username" : username, "Password" : password})
                        else:
                            #If the file exists then appending the data in the file
                            with open("data.csv", "a") as csvfile:
                                writer = csv.DictWriter(csvfile, fieldnames = ["Name", "Age", "Gender", "Username", "Password"])
                                writer.writerow({"Name" : name, "Age": age, "Gender" : gender, "Username" : username, "Password" : password})
                        print("\n\n\t\tCongratulations! You have signed up successfully!!\nPlease Login to use Health Buddy")
                    else:
                        #password didn't meet the required specifications
                        print("Password Error")
                case 3:
                    #Admin log in
                    a_uname = input("Enter Admin Username: ")
                    a_password = input("Enter Password: ")
                    if adminLoginValidator(a_uname, a_password):
                        #If log in successful the calling the main menu
                        adminMenu()

                case 4:
                    #Exiting the project
                    sys.exit(0)
                case _:
                    print("Please enter a valid option number")
            ch = input("\n\nDo you want to go to the Main Menu? \nPress 'y' to go to the main menu and 'n' to exit this application: ").lower()
            if ch in ["yes", "y"]:
                pass
            else:
                sys.exit(0)
        except ValueError:
            print("Please enter number only")
            sys.exit(1)

if __name__ == "__main__":
    main()