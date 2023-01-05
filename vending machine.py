#creating a vending machine

print("Hello")
print("WELCOME TO CHOCOPEDIA AND DRINKSIFY")
print("Languages=  English / Urdu")


#Select a language
Language = {
   '1': 'English',
   '2': 'Urdu'
}
Language_code=input('Please Select The Language:')
if Language_code== 'English': 
    print("You have selected English")         
elif Language_code=='Urdu':
    print("You have selected Urdu")

#Codes of the Items in the shop

items={
    'A121':'kitkat',
    'B131':'dairymilk',
    'C141':'mars',
    'D151':'snickers',
    'E161':'Kinder',
    'F171':'Flake',
    'G181':'Bounty',
    'H191':'Galaxy',
    'I222':'Apple Juice',
    'J333':'Orange Juice',
    'K444':'Strawberry Juice',
    'L555':'Pineapple Juice',
    'M666':'Litchi Drink',
    'N777':'Mango Juice',
    'O888':'Black Coffee',
    'P999':'Water',
   
}

# Menu Of The Shop
print("MENU OF CHOCOPEDIA AND DRINKSIFY")

print("1. Dairymilk Price 8 Rs. , Code:B131")
print("2. Mars price 5 Rs. , Code: C141")
print("3. Snickers Price 4 Rs. , Code: D151")
print("4. Kinder Price 6Rs. , Code: E161")
print("5. Flake Price 3Rs. , Code:F171")
print("6. Bounty Price 5Rs. , Code:G181")
print("7. Galaxy Price 9Rs. , Code:H191")
print("8. Apple Juice Price 10Rs. , Code:I222") 
print("9. Orange Juice Price 12 Rs. , Code:J333")
print("10. Strawberry Juice Price 14Rs. , Code:K444")
print("11. Pineapple Juice Price 17 Rs. , Code:L555")
print("12. Litchi Drink Price 15 Rs. , Code:M666")
print("13. Mango Juice Price 16 Rs. , Code:N777")
print("14. Black Coffee price 20 Rs. , Code: O888")
print("15. Water Price 8 Rs. , Code:P999")


#Price of items    
Dairymilk=8
Mars=5
Snickers=4
Kinder=6
Flake=3
Bounty=5
Galaxy=9
Applejuice=10
Orangejuice=12
Strawberryjuice=14
Pineapplejuice=17
Litchidrink=15
Mangojuice=16
Blackcoffee=20
Water=8

#Code For Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

#Code For Entering the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money"))



#Code for Buying Additional Items   
choice = {
   '1': 'yes',
   '2': 'no'
}
choice=input('would you like to buy some Chips (yes/no):')
if choice== 'yes': 
    print("Thankyou for your Purchase")         
elif Language_code=='no':
    print("OK")

#Code For Returning the Correct Change Of Dairymilk
if items_code=='B131':
 if money >= Dairymilk:
    money=money-Dairymilk


# Code for telling the user how much change they have received.    
    print("Your change is",money)
    
    print("Your order has been Dispensed")
    print("Have a Nice Day")
    print("PLEASE VISIT AGAIN") 

    
#Code For Returning the Correct Change Of Mars   
if items_code=='C141':
    if money >= Mars:  
     money=money-Mars


# Code for telling the user how much change they have received.     
    print("Your change is",money)

    print("Your Order has been Dispensed")
    print("Have a Nice Day")
    print("PLEASE VISIT AGAIN") 

#Code For Returning the Correct Change Of Snickers
if items_code=='D151':  
    if money >= Snickers:
      
     money=money-Mars


# Code for telling the user how much change they have received.     
    print("Your change is",money)

    print("Your Order has been Dispensed")
    print("Have a Nice Day")  
    print("PLEASE VISIT AGAIN") 

#Code For Returning the Correct Change Of Kinder
if items_code=='E161':
    if money >= Kinder:
    
     money=money-Kinder


# Code for telling the user how much change they have received.     
    print("Your change is",money)

    print("Your Order has been Dispensed")
    print("Have a Nice Day")
    print("PLEASE VISIT AGAIN") 

#Code For Returning the Correct Change Of Flake
if items_code=='F171':
     if money >= Flake:
    
      money=money-Flake


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN") 

#Code For Returning the Correct Change Of Bounty
if items_code=='G181':
     if money >= Bounty:
    
      money=money-Bounty

# Code for telling the user how much change they have received.
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN") 

#Code For Returning the Correct Change Of Galaxy
if items_code=='H191':
     if money >= Galaxy:
    
      money=money-Galaxy


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN") 


#Code For Returning the Correct Change Apple Juice
if items_code=='I222':
     if money >= Applejuice:
    
      money=money-Applejuice

# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN") 


#Code For Returning the Correct Change Of Orange Juice
if items_code=='J333':
     if money >= Orangejuice:
    
      money=money-Orangejuice


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN") 


#Code For Returning the Correct Change Of Strawberry Juice
if items_code=='K444':
     if money >= Strawberryjuice:
    
      money=money-Strawberryjuice


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN")  



#Code For Returning the Correct Change Of Pineapple Juice
if items_code=='L555':
     if money >= Pineapplejuice:
    
      money=money-Pineapplejuice


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")     
     print("PLEASE VISIT AGAIN") 



#Code For Returning the Correct Change Of Litchi Drink
if items_code=='M666':
     if money >= Litchidrink:
    
      money=money-Litchidrink


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")  
     print("PLEASE VISIT AGAIN") 


#Code For Returning the Correct Change Mango Juice
if items_code=='N777':
     if money >= Mangojuice:
    
      money=money-Mangojuice


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day")     
     print("PLEASE VISIT AGAIN") 


#Code For Returning the Correct Change Of Black Coffee
if items_code=='O888':
     if money >= Blackcoffee:
    
      money=money-Blackcoffee


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order has been Dispensed")
     print("Have a Nice Day") 
     print("PLEASE VISIT AGAIN") 



#Code For Returning the Correct Change Of Water
if items_code=='P999':
     if money >= Water:
    
      money=money-Water


# Code for telling the user how much change they have received.      
     print("Your change is",money)

     print("Your Order Has Been Dispensed")
     print("Have a Nice Day")
     print("PLEASE VISIT AGAIN")  


     


