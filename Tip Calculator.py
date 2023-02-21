print("Welcome to the Tip Calculator!")
bill_price = float(input("What was the total bill price? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent? "))
split = int(input("How many people will be splitting the bill? "))

tip_percentage = (tip / 100)
tip_percentage_price =  bill_price * tip_percentage
total_bill_price = bill_price + tip_percentage_price
split_bill = (total_bill_price / split)
bill_split_final = round(split_bill, 2)
bill_split_final = "{:.2f}".format(bill_split_final)

print(f"Each person should pay: ${bill_split_final}")