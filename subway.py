def display_menu():
    print("Welcome to the Subway!")
    print("Please choose your sandwich:")
    print("1. Veggie Delight - $5.00")
    print("2. Turkey Breast - $6.50")
    print("3. Meatball Marinara - $7.00")
    print("4. Chicken Teriyaki - $7.50")
    print("5. Italian BMT - $8.00")
    print("6. Exit")

def get_sandwich_choice():
    choice = int(input("Enter the number of your choice: "))
    return choice

def get_toppings():
    toppings = []
    print("Choose your toppings (type 'done' when finished):")
    available_toppings = ["Lettuce", "Tomato", "Onion", "Cheese", "Jalapenos", "Olives"]
    
    for topping in available_toppings:
        add_topping = input(f"Do you want {topping}? (yes/no): ").strip().lower()
        if add_topping == 'yes':
            toppings.append(topping)
    
    return toppings

def calculate_total(choice, toppings):
    prices = {1: 5.00, 2: 6.50, 3: 7.00, 4: 7.50, 5: 8.00}
    sandwich_price = prices.get(choice, 0)
    total = sandwich_price + (0.50 * len(toppings))  # $0.50 for each topping
    return total

def main():
    while True:
        display_menu()
        choice = get_sandwich_choice()
        
        if choice == 6:
            print("Thank you for visiting Subway! Goodbye!")
            break
        
        if choice < 1 or choice > 5:
            print("Invalid choice. Please try again.")
            continue
        
        toppings = get_toppings()
        total = calculate_total(choice, toppings)
        
        print(f"\nYou ordered: Sandwich #{choice}")
        print(f"Toppings: {', '.join(toppings) if toppings else 'None'}")
        print(f"Total cost: ${total:.2f}\n")

if __name__ =="__main__":
    main()