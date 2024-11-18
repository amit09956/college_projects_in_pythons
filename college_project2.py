def addItems(items):
    # Function to add item to the cart
    cart = {}
    while True:
        choice = input("Enter the item name or Done to stop adding items: ").capitalize()
        if choice == 'Done':
            break
        elif choice in items:
            quantity = getQuantity()
            if choice in cart:
                cart[choice] = cart[choice] + quantity
                print(f'{choice} updated by {quantity}')
            else:
                cart[choice] = quantity
                print(f'{choice} added to cart!')
        else:
            print("Item not available.")
    return cart

def display(cart):
    # Function to display the cart
    print("Items in the cart:")
    for item, quantity in cart.items():
        print(f'{item}: {quantity}')
    print()
    
def totalCost(cart, prices):
    # Function to calculate the total cost of the items in the cart
    total = 0
    for item, quantity in cart.items():
        total += prices[item] * quantity
    return total

def removeItems(cart):
    # Function to remove items from the cart
    while True:
        choice = input("Enter the item name to remove or Done to stop removing items: ").capitalize()
        if choice == 'Done':
            break
        elif choice in cart:
            quantity = getQuantity()
            if quantity >= cart[choice]:
                del cart[choice]
                print(f'{choice} removed from cart!')
            else:
                cart[choice] = cart[choice] - quantity
                print(f'{quantity} {choice} removed from cart!')
        else:
            print("Item not in cart.")
    return cart

def applyDiscount(total):
    # Function to apply discount on the total cost
    discount = 0
    if total > 500:
        discount = 0.1 * total
    elif total > 1000:
        discount = 0.2 * total
    elif total > 1500:
        discount = 0.3 * total
    else:
        discount = 0
    total = total - discount
    print("TOTAL COST AFTER DISCOUNT: ", total)
    print("THANK YOUR FOR SHOPPING WITH US!")

def checkout(cart, prices):
    # Function to checkout the items in the cart
    display(cart)
    total = totalCost(cart, prices)
    print()
    print("CHECKOUT")
    print(f"TOTAL COST BEFORE DISCOUNT: {total}")
    total = applyDiscount(total)
    return total

def getQuantity():
    # Function to get the quantity of the item
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity should be greater than 0.")
        except ValueError:
            print("Quantity should be a number.")
        
def main():
    items = ['Apples', 'Mosambi', 'Anar', 'Mango', 'Kiwi']
    prices = { 'Apples': 20, 'Mango': 45.7, 'Kiwi': 100, 'Anar': 40, 'Mosabmi': 22.8}
    
    print("\nWelcome to the Virtual Shopping Cart!\n")
    print("Available items:")
    for i in prices:
        print(f"{i}: {prices[i]}")
    print()
    cart = addItems(items)
    display(cart)
    rem = input("Do you want to remove items or change their quantity? (Y/N): ").upper()
    if rem == 'Y':
        cart = removeItems(cart)
        display(cart)
    else:
        print("No items removed.")

    if cart:
        checkout(cart, prices)
    else:
        print("The cart is empty.")

main()