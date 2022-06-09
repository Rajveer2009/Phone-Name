#!/bin/python3

#improting libraries 
import phonenumbers
from phonenumbers import carrier, geocoder

#main

n = 1

def banner():
        print  ("""\033[94m
████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        \033""")

def do():
    banner()
    print("CTRL + z for exit")
    number = "+91" + input("What phone number do you wanna\nknow info about? ")
    phoneNumber = phonenumbers.parse(number)
    Carrier = carrier.name_for_number(phoneNumber, 'en')
    Region = geocoder.description_for_number(phoneNumber, 'en')
    print(phoneNumber)
    print(Carrier)
    print(Region)

do() 