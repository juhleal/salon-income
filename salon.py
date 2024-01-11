import random

# Function to display the list of services and their prices
def display_services(service_prices):
    print("\n Hair Salon Services:")
    for service, price in service_prices.items():
        print(f"{service}: £{price:.2f}")

# Function to get the number of services done
def get_services_done(service_prices):
    services_done = {}
    for service in service_prices:
        while True:
            try:
                quantity = int(input(f"\n How many times did you do {service} this month? "))
                if quantity < 0:
                    raise ValueError("\n Quantity should be a non-negative integer.")
                services_done[service] = quantity
                break
            except ValueError as e:
                print(f"\n Invalid input. {e}")
    return services_done

# Function to calculate the total amount excluding 20%
def calculate_total_amount(service_prices, services_done):
    total_amount = sum(service_prices[service] * services_done[service] for service in service_prices)
    discount = 0.2 * total_amount
    final_total = total_amount - discount
    return final_total

# Main program
if __name__ == "__main__":
    # Define services and their prices (you can modify these)
    services_and_prices = {
        " Gents Cut": 55.0,
        " Ladies Cut": 90.0,
        " Blow Dry": 65.0,
        " Hair up": 85.0,
        " Balayage": 170.0,
        " Highlights": 185.0,
        " Half Head Highlights": 165.0,
        " Toner": 30.0,
        " Olpaplex": 40.0,
        " Fringe Trim": 15.0,
        " Keratin Treatment": 150.0,
        " Tint": 85.0,
    }

    # Display services and prices
    display_services(services_and_prices)

    # Get the number of services done
    services_done_count = get_services_done(services_and_prices)

    # Calculate the final total amount
    final_total_amount = calculate_total_amount(services_and_prices, services_done_count)

    # Display the final total amount
    print(f"\n Your total amount (excluding 20% discount) is: £{final_total_amount:.2f}\n")
