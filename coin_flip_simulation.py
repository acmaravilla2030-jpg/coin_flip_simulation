import random

# This program simulates a fair coin flip.
# It runs locally, does not collect or store any user data,
# and respects user privacy and ethical programming practices.

def flip_coin():
    """
    Simulates a single coin flip.

    Returns:
        str: 'Heads' or 'Tails'
    """
    return random.choice(["Heads", "Tails"])


def run_simulation(number_of_flips):
    """
    Runs the coin flip simulation multiple times and
    displays a summary of the results.

    Args:
        number_of_flips (int): Number of coin flips to perform
    """
    heads_count = 0
    tails_count = 0

    for i in range(number_of_flips):
        result = flip_coin()
        print(f"Flip {i + 1}: {result}")

        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print("\n--- Summary ---")
    print("Heads:", heads_count)
    print("Tails:", tails_count)


def main():
    """
    Main function that handles user input and
    starts the coin flip simulation.
    """
    try:
        flips = int(input("How many times would you like to flip the coin? "))
        if flips <= 0:
            print("Please enter a number greater than zero.")
        else:
            run_simulation(flips)
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
