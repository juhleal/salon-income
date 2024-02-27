import random

# Function to display the list of services and their prices
def display_services(service_prices):
    """
    Displays the list of available hair salon services along with their respective prices.

    Args:
    - service_prices (dict): A dictionary mapping each service to its price.
    """
    print("\nHair Salon Services:")
    for service, price in service_prices.items():
        print(f"{service}: £{price:.2f}")

# Function to get the number of services done
def get_services_done(service_prices):
    """
    Asks the user for the number of times each service has been done this month.

    Args:
    - service_prices (dict): A dictionary mapping each service to its price.

    Returns:
    - services_done (dict): A dictionary mapping each service to the number of times it's been done.
    """
    services_done = {}
    for service in service_prices:
        while True:
            try:
                quantity = int(input(f"\nHow many times did you do {service} this month? "))
                if quantity < 0:
                    raise ValueError("\nQuantity should be a non-negative integer.")
                services_done[service] = quantity
                break
            except ValueError as e:
                print(f"\nInvalid input. {e}")
    return services_done

# Function to calculate the total amount excluding 20%
def calculate_total_amount(service_prices, services_done):
    """
    Calculates the total amount for the services done, excluding a 20% discount.

    Args:
    - service_prices (dict): A dictionary mapping each service to its price.
    - services_done (dict): A dictionary mapping each service to the number of times it's been done.

    Returns:
    - final_total (float): The final total amount after applying the discount.
    """
    total_amount = sum(service_prices[service] * services_done[service] for service in service_prices)
    discount = 0.2 * total_amount
    final_total = total_amount - discount
    return final_total

# Main program
if __name__ == "__main__":
    # Define services and their prices
    services_and_prices = {
        "Gents Cut": 55.0,
        "Ladies Cut": 90.0,
        "Blow Dry": 65.0,
        "Hair up": 85.0,
        "Balayage": 170.0,
        "Highlights": 185.0,
        "Half Head Highlights": 165.0,
        "Toner": 30.0,
        "Olpaplex": 40.0,
        "Fringe Trim": 15.0,
        "Keratin Treatment": 150.0,
        "Tint": 85.0,
    }

    # Display services and prices
    display_services(services_and_prices)

    # Get the number of services done
    services_done_count = get_services_done(services_and_prices)

    # Calculate the final total amount
    final_total_amount = calculate_total_amount(services_and_prices, services_done_count)

    # Display the final total amount
    print(f"\nYour total amount (excluding 20% discount) is: £{final_total_amount:.2f}\n")
