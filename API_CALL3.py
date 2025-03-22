

import requests
import json



'''
TASK 3 : Connect to this API endpoint https://randomuser.me/api/?results=500
Extract all male and female profiles into a different list
At the end you should have 2 lists , one for male and the other for female.
Extract all dob date into a list.
You will see the dob key with a value containing 2 keys date and age. We are only interested in the date.
Extract that date into a list
Extract concatenated first name and last name into a list
This means you will find a way to extract the first name, last name and concatenate them together to make a full name, make sure you send the full name into a list.

'''
# Extract all male and female profiles into a different list .At the end you should have 2 lists , one for male and the other for female.

# API endpoint to fetch random users
url = 'https://randomuser.me/api/?results=500'
#Parse API response as JSON
response3 = requests.get(url)

Total_response = response3.json()

Total_response['results']

final = Total_response['results']

# Initialize lists to store categorized user information
Info_male = []
Info_female = []

# Categorizing users based on gender
for bio in final:
    if bio['gender']== 'female':
        Info_female.append(bio)
    elif bio['gender']== 'male':
        Info_male.append(bio)    
# Print categorized lists
print(Info_female)  
print(Info_male)

#Extract all dob date into a list. You will see the dob key with a value containing 2 keys date and age. We are only interested in the date.
''''
FEMALE_INFO
'''
# Extract Date of Birth (DOB) for Female Users
new_female_info = []
for information in Info_female:
    dat = information['dob']
    new_female_info.append(dat)

print(new_female_info )

#Extract that date into a list
female_info_outcome = []
for updated_female_info in new_female_info:
    F = updated_female_info['date']
    female_info_outcome.append(F)

print(female_info_outcome  )



#Extract all dob date into a list. You will see the dob key with a value containing 2 keys date and age. We are only interested in the date.

''''
MALE_INFO
'''
# Extract Date of Birth (DOB) for male Users
new_male_info = []
for information in Info_male:
    dat = information['dob']
    new_male_info.append(dat)

print(new_male_info )  

#Extract that date into a list
male_info_outcome = []
for updated_male_info in new_male_info:
    M = updated_male_info['date']
    male_info_outcome.append(M)

print(male_info_outcome)


# Extract concatenated first name and last name into a list
#This means you will find a way to extract the first name, last name and concatenate them together to make a full name, make sure you send the full name into a list.

''''
MALE_INFO
'''

check_name = []
for names in Info_male:
    mm = names['name']
    check_name.append(mm)
print(check_name)    
# Extract and Concatenate Full Names for Male Users
male_fullname = []
for correctname in check_name:
    x = correctname['first']
    y = correctname['last']
    result  = x +" " + y
    male_fullname.append(result)

   
print(male_fullname ) 


# Extract concatenated first name and last name into a list
#This means you will find a way to extract the first name, last name and concatenate them together to make a full name, make sure you send the full name into a list.

''''
FEMALE_INFO
'''
check_name_w = []
for names in Info_female:
    ff = names['name']
    check_name_w.append(ff)
print(check_name_w)


# Extract and Concatenate Full Names for female Users
female_fullname = []
for correctname_w in check_name_w:
    xw = correctname_w['first']
    yw = correctname_w['last']
    result_w  = xw +" " + yw
    female_fullname.append(result_w)

   
print(female_fullname   )
