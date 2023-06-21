"""Problem stateme:You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them!
Given the total number of kaleidoscopes that a customer buys, let them know what their total will be. Tax is 7%. All of your kaleidoscopes cost the same amount, 5.00"""

k=int(input("Enter the Number of Kaleidoscopes you bought "))
Total = 5*k
if k > 1:
   Discount  = Total -(0.1*Total)
   Tax=Discount+(0.07*Discount)
   print(("Therefore total would be %.2f")% (Tax))
else:
   Tax=Total +(0.07*Total)
   print(("Without Discount %.2f")%(Tax))