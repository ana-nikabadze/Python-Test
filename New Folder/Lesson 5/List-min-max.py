# შექმენით ცარიელი ლისტი, რომელსაც შეავსებთ შემთხვევითი რიცხვებით, დაბეჭდეთ ელემენტებიდან მინიმალური და მაქსიმალური მნიშვნელობები

import random
mylist = [random.randint(1, 50) for _ in range(10)]
print (mylist)
mylist_min = min(mylist)
mylist_max = max(mylist)
print (mylist_min, mylist_max)


# ირაკლი ძალიან დატვირთული კვირა მქონდა და სამწუხაროდ 5-დან მარტო 3 დავალება მოვასწარი. დანარჩენებს ჩემთვის გავაკეთებ მოგვიანებით. 
# რაც მოვასწარი პირველ სამს გიგზავნი. 