
#this line is to assist with understanding the code
#file to be saved
# ## # print("hello fintech! I changed it!!!")


#testing save feature
company_ABC = 75.5
print(company_ABC)

TriConn_stock_price = 88.56

#adjusted_price takes into account trade fees

adjusted_price = TriConn_stock_price - 1.56
print (TriConn_stock_price, adjusted_price)

print(f'The current price is {TriConn_stock_price}, but adjusted for commissions it is {adjusted_price}')


# 5. @TODO: Print all of the variables.
# YOUR CODE HERE!
# 1. @TODO: Create a variable called `original_price`
# and assign it the value of `198.87`.
initial_price = 198.87

# 2. @TODO: Create a variable called `current_price`
# and assign it the value `254.32`.
current_price = 254.32

# 3. @TODO: Create a variable called `increase` and assign the
# difference between the current price and the original price.
intra_day_delta = current_price - initial_price

# 4. @TODO: Divide `increase` by `original_price` and multiply that by 100.
# Then assign the results to the variable called `percent_increase`.
delta_percent = intra_day_delta/initial_price*100

# 5. @TODO: Print all of the variables.
print (initial_price, current_price, intra_day_delta, delta_percent)

best_places_to_eat = ["five_guys", "smash_burger", "au_bon_pain", "sushi_ya", "shake_shack"]

#print (best_places_to_eat)
#print (best_places_to_eat[0])
#print (best_places_to_eat[3])
all_time_best = best_places_to_eat[0]
second_best_eat = best_places_to_eat[4]
print (all_time_best, second_best_eat)
print (best_places_to_eat[0:4])

#empty list exercise

list_of_FAANG = []

list_of_FAANG.append ("Apple")
list_of_FAANG.append ("GOOG"), 
list_of_FAANG.append ("Facebook")
list_of_FAANG.append ("Amazon")
list_of_FAANG.append ("Netflix")
list_of_FAANG.append (best_places_to_eat)
print (list_of_FAANG)

closing_prices = [12.3, 12.8, 12.54, 12.9, 12.01]

highest_price = max (closing_prices)

print (highest_price)

lenght_of_list = len(closing_prices)

print(lenght_of_list, f'ADDED SPACE PLZ', f'we can also say {len(closing_prices)}')


