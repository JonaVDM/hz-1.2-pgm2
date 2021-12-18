import math


def main() -> None:
    """The main user-interaction loop"""
    prices: list[float] = [30, 10, 20]

    while True:
        print("="*50)
        print("\nDe lijst is", prices)
        menu()
        inp = input("Maak een keuze: ")
        choice = 1

        try:
            choice = int(inp)
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue

        print("\n")

        if choice == 9:
            break

        prices = do_action(choice, prices)
        print("\n")


def menu() -> None:
    """A function that simply prints the menu"""
    print("""
(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

    """)


def do_action(action: int, prices: list) -> list:
    """ Checks which action it should do and performs it
    """
    if action == 0:
        return new_list(prices)
    elif action == 1:
        print_stocks(prices)
    elif action == 2:
        print_average(prices)
    elif action == 3:
        print_standard_deviation(prices)
    elif action == 4:
        print_minimum(prices)
    elif action == 5:
        print_maximum(prices)
    elif action == 6:
        print_tri(prices)
    else:
        print("Geen geldige input, probeer het opnieuw!")
    return prices


#
# -- Menu item functions --
#

def new_list(current: list) -> list:
    """ asks the user for a new list and parses this
    """
    inp = input("Voer een nieuwe lijst in: ")
    try:
        new_L = eval(inp)
        if isinstance(new_L, list):
            return new_L
        print("Dat lijkt geen lijst. L wordt niet aangepast.")
    except:
        print("Ik begreep de invoer niet. L wordt niet aangepast.")
    return current


def print_stocks(prices: list) -> None:
    """ Makes a fancy list of all the prices
    """
    print(f"{'Dag'}  {'Prijs'}")
    print("-" * 10)
    for day, price in enumerate(prices):
        print(f"{day: >3} {price: .2f}")


def print_average(prices: list) -> None:
    """ Print out the average price
    """
    print(f"De gemiddelde prijs is {get_average(prices): .2f}")


def print_standard_deviation(prices: list) -> None:
    """ Print out the standard deviation
    """
    print(f"De standaardafwijking is {get_standard_deviation(prices)}")


def print_minimum(prices: list) -> None:
    """ Prints the minimum value together with the day
    """
    price, day = get_minimum(prices)
    print(f"Het minimum is {price} op dag {day}")


def print_maximum(prices: list) -> None:
    """ Prints the minimum value together with the day
    """
    price, day = get_maximum(prices)
    print(f"Het maximum is {price} op dag {day}")


def print_tri(prices: list) -> None:
    buy, sell = get_tri(prices)
    print(f"Koop op dag {buy} voor {prices[buy]}")
    print(f"Verkoop op dag {sell} voor {prices[sell]}")
    print(f"Voor een totale winst van {prices[sell] - prices[buy]}")


#
# -- Help functions --
#


def get_average(prices: list) -> float:
    """ Returns the average value of a list of floats
    """
    return get_sum(prices) / len(prices)


def get_sum(prices: list) -> float:
    """ Returns the sum of the list
    """
    total = 0.0
    for price in prices:
        total += price
    return total


def get_standard_deviation(prices: list) -> float:
    """ Returns the standard deviation of the list
    """
    total = 0.0
    average = get_average(prices)

    for price in prices:
        total += (price - average) ** 2

    return math.sqrt(total / len(prices))


def get_minimum(prices: list) -> tuple:
    """ Returns the smallest price together with the day
    """
    small = prices[0]
    day = 0
    for d, p in enumerate(prices):
        if small > p:
            day = d
            small = p

    return (small, day)


def get_maximum(prices: list) -> tuple:
    """ Returns the highest price together with the day
    """
    big = prices[0]
    day = 0
    for d, p in enumerate(prices):
        if big < p:
            day = d
            big = p

    return (big, day)


def get_tri(prices: list) -> tuple:
    """ Returns the most profit that could have been made
        if we happened to own a timemachine
    """
    buy_date = -1
    sell_date = -1
    profit = -1

    for day, price in enumerate(prices):
        for i in range(day + 1, len(prices)):
            if prices[i] - price > profit:
                buy_date = day
                sell_date = i
                profit = prices[i] - price

    return buy_date, sell_date
