#0.9 Yard Greening
SQM_PRICE = 7.61
discount = 0.18 # Offering 18% Discount 

#sqm = Square Meters
sqm = float(input())

greeningPrice = sqm * SQM_PRICE #1
discountPrice = discount * greeningPrice #2
sum = greeningPrice - discountPrice #3

print(f"The final price is: {sum} lv.")
print(f"The discount is: {discountPrice} lv.")