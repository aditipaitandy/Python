# Input the number of days the book was used
days =int(input("Enter nummber of days used:  "))
fee = 0

if days <= 5:
    fee = days * 2  # Rs 2 per day
elif 6 <= days <= 10:
    fee = (5 * 2) + ((days - 5) * 3)  # Rs 2 for first 5 days, Rs 3 for the next days
elif 11 <= days <= 15:
    fee = (5 * 2) + (5 * 3) + ((days - 10) * 4)  # Rs 2 for first 5 days, Rs 3 for next 5, Rs 4 for the next days
else:
    fee = (5 * 2) + (5 * 3) + (5 * 4) + ((days - 15) * 5)  # Rs 2 for first 5, Rs 3 for next 5, Rs 4 for next 5, Rs 5 thereafter

# Output the total fee
print(f'Total fee for {days} days: Rs {fee}')
