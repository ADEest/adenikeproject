# Import the random, uuid, and requests modules
import random
import uuid
import requests
import random
import string
import time
# Import the csv module
import csv

# Create a function that generates a particular number of data based on the info and store in a csv format


def generate_data(n):
    # Create a list of provinces in the USA
    provinces = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
                 "Colorado", "Connecticut", "Delaware", "Florida", "Georgia"]
    # Create a list of possible genders
    genders = ["male", "female"]
    # Create a list of possible countries
    countries = ["USA"]
    # Create a list of possible addresses
    addresses = ["1 Mercury Street", "2 Venus Avenue", "3 Earth Road", "4 Mars Lane", "5 Jupiter Drive", "6 Saturn Circle", "7 Uranus Place", "8 Neptune Way", "9 Pluto Court", "10 Sun Terrace",
                 "11 Moon Crescent", "12 Star Boulevard", "13 Comet Trail", "14 Asteroid Alley", "15 Galaxy Park", "16 Meteor Close", "17 Planet Square", "18 Solar View", "19 Lunar Rise", "20 Cosmic Ridge"]
    # Create a list of possible firstnames
    firstname = ["Emily", "Diana", "Elmira", "Abraham", "Dave", "John", "Mary", "Alice", "Bob", "Emma", "Daniel", "Sarah", "James", "Anna", "Michael", "Laura", "David", "Lisa", "Robert", "Amy", "William", "Rebecca", "Thomas", "Rachel", "Charles", "Nicole", "Mark", "Jessica", "Steven", "Samantha", "Paul", "Jennifer", "Andrew", "Emily", "Richard", "Michelle", "Kevin", "Angela", "Brian", "Melissa", "Edward", "Kelly", "Anthony", "Kimberly", "Jason", "Christina", "Ryan", "Amanda",
                 "Eric", "Heather", "Adam", "Stephanie", "Patrick", "Elizabeth", "Scott", "Megan", "Timothy", "Hannah", "Joshua", "Ashley", "Justin", "Alexis", "Brandon", "Brittany", "Nathan", "Taylor", "Aaron", "Lauren", "Gregory", "Kayla", "Sean", "Victoria", "Jeremy", "Jasmine", "Kyle", "Madison", "Zachary", "Hailey", "Ethan", "Olivia", "Tyler", "Abigail", "Cody", "Isabella", "Dylan", "Sophia", "Jordan", "Avery", "Connor", "Chloe", "Noah", "Lily", "Evan", "Ella", "Cameron", "Grace"]
    # Create a list of possible lastnames
    lastname = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
                "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"]
    # Create an empty list to store the data
    data = []
    # Loop n times to generate n data
    for i in range(n):
        # Randomly select a firstname, lastname, gender, country and address
        fname = random.choice(firstname)
        lname = random.choice(lastname)
        gender = random.choice(genders)
        country = random.choice(countries)
        address = random.choice(addresses)
        province = random.choice(provinces)
        # Randomly select an age between 18 and 40
        age = random.randint(18, 40)
        # Generate a random blockchain wallet address
        # For simplicity, we use a random hexadecimal string of 40 characters
        blockchain_wallet_address = "".join(
            random.choice("0123456789abcdef") for i in range(40))
        # Generate a random voters ID
        # For simplicity, we use a UUID (universally unique identifier)
        voters_id = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=random.randint(9, 10)))
        # Generate a random government ID number
        # For simplicity, we use another UUID
        government_id_number = str(int(time.time() * 1000)) + ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=5))
        # Get the voter's IP address and device information
        # For simplicity, we use a free API service that returns these data
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json()["ip"]
        response = requests.get(f"https://ipinfo.io/{ip_address}")

        # Generate a random marital status
        # For simplicity, we use a list of possible values
        marital_status = random.choice(
            ["Single", "Married", "Divorced", "Widowed"])
        # Generate a random political affiliation
        # For simplicity, we use a list of possible values
        political_affiliation = random.choice(
            ["Labour group", "Conservative", "Liberal", "Independent", "None"])
        # Generate a random occupation
        # For simplicity, we use a list of possible values
        occupation = random.choice(["Teacher", "Doctor", "Lawyer", "Engineer", "Accountant",
                                   "Nurse", "Student", "Farmer", "Trader", "Driver", "Unemployed"])
        # Generate a random email
        # For simplicity, we use the firstname and lastname and a random domain
        email = fname.lower() + "." + lname.lower() + "@" + \
            random.choice(["gmail.com", "yahoo.com",
                          "hotmail.com", "outlook.com"])
        # Generate a random phone number
        # For simplicity, we use a random string of 10 digits
        phone = "".join(random.choice("0123456789") for i in range(10))
        # Create a dictionary with the selected values
        record = {"FirstName": fname, "LastName": lname, "Gender": gender, "Country": country, "Address": address, "Age": age, "BlockchainWalletAddress": blockchain_wallet_address, "VotersID": voters_id,
                  "GovernmentIDNumber": government_id_number, "IPAddress": ip_address,  "MaritalStatus": marital_status, "PoliticalAffiliation": political_affiliation, "Occupation": occupation, "Email": email, "Phone": phone, "Province": province}
        # Append the dictionary to the data list
        data.append(record)
    # Open a csv file with write mode
    with open("data.csv", "w") as f:
        # Create a csv writer object
        writer = csv.DictWriter(f, fieldnames=["FirstName", "LastName", "Gender", "Country", "Address", "Age", "BlockchainWalletAddress",
                                "VotersID", "GovernmentIDNumber", "IPAddress", "MaritalStatus", "PoliticalAffiliation", "Occupation", "Email", "Phone", "Province"])
        # Write the header row
        writer.writeheader()
        # Write the data rows
        writer.writerows(data)
    # Return the data list
    return data


# Test the function with n = 10
data = generate_data(10)
# Print the data
print(data)
