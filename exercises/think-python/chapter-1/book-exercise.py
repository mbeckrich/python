# Suppose the cover price of a book is $24.95, but bookstores get a 40 % discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

book = 24.95
discount = .40
discounted_book = book - (book * discount)
first_shipping = 3
extra_shipping = 0.75
all_books = discounted_book * 60
total_shipping = first_shipping + (extra_shipping * 59)
full_cost = all_books + total_shipping

print("A discounted book costs:")
print(round(discounted_book, 2))  # round( , number) rounds float to number
print("Shipping for the first book costs:")
print(first_shipping)
print('and shipping for the remaining 59 books costs:')
print(extra_shipping * 59)
print("so shipping for all 60 books costs:")
print(total_shipping)
print("The cost of all books and shipping combined is:")
print(round(full_cost, 2))
