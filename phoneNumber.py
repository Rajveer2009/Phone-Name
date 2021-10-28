#improting libraries 
import phonenumbers
from phonenumbers import carrier, geocoder

#defining variables
number = "+91" + input("What phone number do you wanna\nknow info about? ")
phoneNumber = phonenumbers.parse(number)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')

#printing variables
print(phoneNumber)
print(Carrier)
print(Region)
