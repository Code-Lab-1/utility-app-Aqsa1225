

#creating a vending machine

print("Hello")
print("______________________________________________________________")
print("WELCOME TO CHOCOPEDIA AND DRINKSIFY")
print("..............................................................")
print("[Languages=  English / Urdu]")
print("______________________________________________________________")

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
   
    '1111':'dairymilk',
    '2222':'mars',
    '3333':'snickers',
    '4444':'Kinder',
    '5555':'Flake',
    '6666':'Bounty',
    '7777':'Galaxy',
    '8888':'Apple Juice',
    '9999':'Orange Juice',
    '1122':'Strawberry Juice',
    '1133':'Pineapple Juice',
    '1144':'Litchi Drink',
    '1155':'Mango Juice',
    '1166':'Black Coffee',
    '1177':'Water',
   
}

# Menu Of The Shop
print("MENU OF CHOCOPEDIA AND DRINKSIFY")
print("..............................................................")
print("1. Dairymilk             AED 250 ,    Code: 1111 ,   Stock:300")
print("2. Mars                  AED 185 ,    Code: 2222 ,   Stock:350")
print("3. Snickers              AED 135 ,    Code: 3333 ,   Stock:100")
print("4. Kinder                AED 210 ,    Code: 4444 ,   Stock:200")
print("5. Flake                 AED 280 ,    Code: 5555 ,   Stock:350")
print("6. Bounty                AED 275 ,    Code: 6666 ,   Stock:100")
print("7. Galaxy                AED 235 ,    Code: 7777 ,   Stock:150")
print("      ...MENU OF DRINKS...  ")
print("8. Apple Juice           AED 120 ,    Code: 8888 ,   Stock:100") 
print("9. Orange Juice          AED 115 ,    Code: 9999 ,   Stock:200")
print("10. Strawberry Juice     AED 150 ,    Code: 1122 ,   Stock:55")
print("11. Pineapple Juice      AED 130 ,    Code: 1133 ,   Stock:90")
print("12. Litchi Drink         AED 135 ,    Code: 1144 ,   Stock:150")
print("13. Mango Juice          AED 145 ,    Code: 1155 ,   Stock:90")
print("14. Black Coffee         AED 250 ,    Code: 1166 ,   Stock:50")
print("15. Water Price          AED 165 ,    Code: 1177 ,   Stock:200")
print("..............................................................")

#Price of items    
Dairymilk=250
Mars=185
Snickers=135
Kinder=210
Flake=280
Bounty=275
Galaxy=235
Applejuice=120
Orangejuice=115
Strawberryjuice=150
Pineapplejuice=130
Litchidrink=135
Mangojuice=145
Blackcoffee=250
Water=165

# check stock
stock=3000
if stock > 0:
    print("____________________________________________________________________")
    print("We have chocolates and drinks in stock. Please make your selection.")
    print("_____________________________________________________________________")

#Code For Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

#Code For Entering the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money"))



#Code for  Additional Items   
choice = {
   '1': 'yes',
   '2': 'no'
}
choice=input('Chocopedia and Drinksify would like to suggest you to have some biscuits? (ok/no):')
if choice== 'ok': 
    print("...............................")
    print("Thankyou for your Selection")         
elif choice=='no':
    print("Thankyou for your Selection")

#Code For Returning the Correct Change Of Dairymilk
if items_code=='1111':
   if money >= Dairymilk:
    money=money-Dairymilk

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")   
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")

#Code For Returning the Correct Change Of Mars 
if items_code=='2222':
   if money >= Mars:
    money=money-Mars

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  


#Code For Returning the Correct Change Of Snickers
if items_code=='3333':
   if money >= Snickers:
    money=money-Snickers

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  

#Code For Returning the Correct Change Of Kinder
if items_code=='4444':
   if money >= Kinder:
    money=money-Kinder

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")
  
    
 

#Code For Returning the Correct Change Of Flake
if items_code=='5555':
   if money >= Flake:
    money=money-Flake

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  


#Code For Returning the Correct Change Of Bounty
if items_code=='6666':
   if money >= Bounty:
    money=money-Bounty

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  


#Code For Returning the Correct Change Of Galaxy
if items_code=='7777':
   if money >= Galaxy:
    money=money-Galaxy

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Apple Juice
if items_code=='8888':
   if money >= Applejuice:
    money=money-Applejuice

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Of Orange Juice
if items_code=='9999':
   if money >= Orangejuice:
    money=money-Orangejuice

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Of Strawberry Juice
if items_code=='1122':
   if money >= Strawberryjuice:
    money=money-Strawberryjuice

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN.") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  




#Code For Returning the Correct Change Of Pineapple Juice
if items_code=='1133':
   if money >= Pineapplejuice:
    money=money-Pineapplejuice

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  
 



#Code For Returning the Correct Change Of Litchi Drink
if items_code=='1144':
   if money >= Litchidrink:
    money=money-Litchidrink

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Mango Juice
if items_code=='1155':
   if money >= Mangojuice:
    money=money-Mangojuice

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Of Black Coffee
if items_code=='1166':
   if money >= Blackcoffee:
    money=money-Blackcoffee

    print("......................")
    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN") 
   else:
     print("Try Again.Insufficient balance.Money Refunded")  



#Code For Returning the Correct Change Of Water
if items_code=='1177':
   if money >= Water:
    money=money-Water

    print("Your change is",money)
    print("......................")
    print("Your order has been Dispensed")
    print("......................")
    print("Take your Receipt")
    print("......................")
    print("Have a Nice Day")
    print("......................")
    print("PLEASE VISIT AGAIN.Insufficient balance.Money Refunded") 
  
 









     



