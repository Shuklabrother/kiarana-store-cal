#this code help me to calculate the total price of item

#that starting we assume that the total price was 0 rupees
total_cost = 0
#this line of code number of item custom have
no_of_items = int(input("Number of items: "))
#this "for i in range(no_of_items):" is a loop that number of time we repate the code
for i in range(no_of_items):
  #this line of code "product = input("Enter the product name: ")" we ask custom what is name of product
    product = input("Enter the product name: ")
  #this line of code "number = int(input("Enter the number: "))" we ask custom what is number of product
    number = int(input("Enter the number: "))
  #this line of code " price = float(input("Enter the price: "))" we ask custom what is price of product
    price = float(input("Enter the price: "))
    #this line of code "item_cost = number * price" we calculate the item cost of product
    item_cost = number * price
   #this line of code " total_cost += item_cost" we calculate the total cost 
    total_cost += item_cost
    print(f"Cost of {product}: {item_cost}")

print(f"Total cost: {total_cost}")
