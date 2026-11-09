# need to import datetime so we can get todays date for the reciept later
import datetime

# 1. making my store stuff
# a dictionary holding my 5 products and how much they cost
products = {
    "Comic Book": 4.50,
    "Action Figure": 12.00,
    "Trading Cards": 3.00,
    "Poster": 8.50,
    "T-Shirt": 15.00
}

# 2. the shopping cart
# making an empty dictionary for cart so we can put stuff in it later
shopping_cart = {}


# function 1: shows the products to the user (it takes a parameter)
def show_available_products(inv):
    # print a menu title thing
    print("\n--- Available Products ---")
    # start counting at 1 cuz starting at 0 is weird for regular people
    counter = 1
    # loop thru the items in dictionary using .items()
    for name, price in inv.items():
        # print it out and make the money look right with 2 decimals
        print(f"{counter}. {name} - ${price:.2f}")
        # add 1 to counter for the next loop
        counter += 1


# function 2: gets the subtotal (has parameters and returns a value)
def calculate_subtotal(cart, inv):
    # total starts at 0 
    total = 0.0
    # loop over the cart dictionary
    for name, qty in cart.items():
        # get the price from my other dictionary
        price = inv[name]
        # multiply price and quantity to get how much this cost
        line_total = price * qty
        # add it to the big total
        total += line_total
    # give the total back to where it was called from
    return total


# function 3: figure out the discount (has parameter and return value)
def get_discount_rate(amount):
    # if they spend less than 10 bucks
    if amount < 10.00:
        # no discount for u
        return 0.0
    # if they spend between 10 and 20
    elif amount >= 10.00 and amount < 20.00:
        # 5 percent discount
        return 0.05
    # if they spend 20 to 40
    elif amount >= 20.00 and amount < 40.00:
        # 10 percent discount
        return 0.10
    # if its none of those it means they spend over 40
    else:
        # 15 percent discount
        return 0.15


# function 4: shows what is in the cart (has parameters)
def display_cart(cart, inv):
    # check if length of cart is 0 which means its empty
    if len(cart) == 0:
        # tell them its empty
        print("\nYour shopping cart is empty.")
    else:
        # print the top part of the cart
        print("\nYOUR SHOPPING CART")
        print(f"{'Product':<15} {'Unit Price':<12} {'Quantity':<10} {'Line Total'}")
        
        # this keep track of how many things they buy
        total_items = 0
        
        # go thru the cart
        for name, qty in cart.items():
            # look up price
            price = inv[name]
            # math to get the line total
            line_total = price * qty
            # add to my item counter
            total_items += qty
            # print out all the info with formatting so it looks straight
            print(f"{name:<15} ${price:<11.2f} {qty:<10} ${line_total:.2f}")

        # print total items at bottom
        print(f"\nTotal Items: {total_items}")
        # call my function to do the math for subtotal
        sub = calculate_subtotal(cart, inv)
        # print the subtotal with the 2 decimals
        print(f"Subtotal: ${sub:.2f}")


# function 5: prints the receipt at the very end (has parameters)
def print_receipt(cart, inv):
    # get the subtotal from my function
    subtotal = calculate_subtotal(cart, inv)
    # get the discount rate from my other function
    discount_rate = get_discount_rate(subtotal)
    
    # math to see how much money they save
    saved = subtotal * discount_rate
    # math to get the real final total
    final_total = subtotal - saved

    # print title of reciept
    print("\nRECEIPT")
    
    # this gets the current date stuff from datetime
    today = datetime.datetime.now()
    # make it look like Month/Day/Year
    date_string = today.strftime("%m/%d/%Y")
    # print the date we just made
    print(f"Date: {date_string}\n")

    # counter for items again
    total_items = 0
    # print the headers for the columns
    print(f"{'Product':<15} {'Unit Price':<12} {'Quantity':<10} {'Line Total'}")
    
    # loop to print cart items again on the reciept
    for name, qty in cart.items():
        # get price
        price = inv[name]
        # get line total
        line_total = price * qty
        # add to items count
        total_items += qty
        # print row
        print(f"{name:<15} ${price:<11.2f} {qty:<10} ${line_total:.2f}")

    # print the final stats at the bottom
    print(f"\nTotal Items:    {total_items}")
    # print subtotal
    print(f"Subtotal:      ${subtotal:.2f}")
    # print discount but multiply by 100 so it looks like a whole number not a decimal
    print(f"Discount:      {int(discount_rate * 100)}%")
    # print how much they saved
    print(f"Amount Saved:  ${saved:.2f}")
    # print the real final total
    print(f"Final Total:   ${final_total:.2f}")
    
    # say thanks
    print("\nThank you for shopping!")


# ==========================================
# MAIN PROGRAM START
# ==========================================

# using a boolean flag so the loop keep going
shopping = True

# 3. main menu loop (while loop 1)
while shopping:
    # print all the menu stuff
    print("\nSMART SHOPPING CART")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    # get what they typed and turn to int
    choice = int(input("\nEnter your choice: "))

    # 4. view products option
    if choice == 1:
        # just call the show function
        show_available_products(products)

    # 5. add stuff to cart
    elif choice == 2:
        # show products first so they know what numbers to type
        show_available_products(products)
        
        # make a list of keys so we can match the number they type to the name
        product_names = list(products.keys())

        # flag to check if they typed a good product number (while loop 2)
        valid_choice = False
        while not valid_choice:
            # ask for number
            prod_num = int(input("Enter product number: "))
            # check if it is 1 to 5
            if prod_num >= 1 and prod_num <= 5:
                # it is good so we can stop loop
                valid_choice = True
            else:
                # it is bad tell them they messed up
                print("Invalid choice. Please enter a number between 1 and 5.")

        # get name from list (minus 1 cuz lists start at 0)
        chosen_name = product_names[prod_num - 1]

        # flag for quantity (while loop 3)
        valid_qty = False
        while not valid_qty:
            # ask how many they want
            qty = int(input(f"How many {chosen_name} would you like to add? "))
            # gotta be more than 0
            if qty > 0:
                # it is good
                valid_qty = True
            else:
                # cant add negative or 0 things
                print("Quantity must be greater than 0.")

        # check if it is already in the dictionary
        if chosen_name in shopping_cart:
            # it is there, so just add more to the quantity
            shopping_cart[chosen_name] += qty
        else:
            # it is not there so make a new entry for it
            shopping_cart[chosen_name] = qty

        # tell them it worked
        print(f"Added {qty} {chosen_name} to your cart!")
        # tell them how much they have total now
        print(f"{chosen_name} quantity is now {shopping_cart[chosen_name]}.")

    # 6. remove stuff
    elif choice == 3:
        # check if cart is empty first cuz we cant remove nothing
        if len(shopping_cart) == 0:
            print("Your cart is empty. Nothing to remove.")
        else:
            # print title
            print("\nYOUR SHOPPING CART")
            
            # make a list of what is in the cart right now
            cart_items = list(shopping_cart.keys())
            
            # counter again
            counter = 1
            # loop thru the list of keys
            for item in cart_items:
                # get the qty from dict
                qty = shopping_cart[item]
                # print out the number and name and qty
                print(f"{counter}. {item} - Quantity: {qty}")
                # plus 1 to counter
                counter += 1

            # flag to check if remove number is good (while loop 4)
            valid_remove = False
            while not valid_remove:
                # ask what to remove
                remove_num = int(input("\nEnter item number to remove: "))
                # check if the number they typed is actually in our list
                if remove_num >= 1 and remove_num <= len(cart_items):
                    # it is good
                    valid_remove = True
                else:
                    # they typed a bad number
                    print("Invalid selection. Try again.")

            # get the item name from list index
            item_to_remove = cart_items[remove_num - 1]
            
            # minus 1 from the quantity in dict
            shopping_cart[item_to_remove] -= 1
            # tell them we took one out
            print(f"Removed 1 {item_to_remove} from your cart!")

            # if the quantity hit 0 we need to delete it from dictionary
            if shopping_cart[item_to_remove] == 0:
                # del deletes the whole key
                del shopping_cart[item_to_remove]
                # let them know its gone
                print(f"{item_to_remove} has been completely removed from the cart.")
            else:
                # if its not 0 just tell them how many are left
                print(f"{item_to_remove} quantity is now {shopping_cart[item_to_remove]}.")

    # 7. view the cart
    elif choice == 4:
        # call the display function
        display_cart(shopping_cart, products)

    # 8. see the current total
    elif choice == 5:
        # check if empty
        if len(shopping_cart) == 0:
            # total is 0
            print("\nYour current subtotal is: $0.00")
        else:
            # call subtotal function and save it
            current_total = calculate_subtotal(shopping_cart, products)
            # print it
            print(f"\nYour current subtotal is: ${current_total:.2f}")

    # 9. checkout and quit
    elif choice == 6:
        # dont let them checkout if they didnt buy nothing
        if len(shopping_cart) == 0:
            # error message
            print("\nYour cart is empty! Please add items before checking out.")
        else:
            # call the receipt function so it print out the reciept
            print_receipt(shopping_cart, products)
            
            # make shopping false so the while loop breaks and program stops
            shopping = False

    # if they typed a letter or something weird on main menu
    else:
        # tell them to type 1 thru 6
        print("Invalid choice. Please enter a number between 1 and 6.")