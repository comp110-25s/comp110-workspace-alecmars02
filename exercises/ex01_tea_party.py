"""Tea Party Planning Program!"""

__author__: str = "730468679"


def main_planner(guests: int) -> None:
    """Planner function to organize the below functions, neat!"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed at the party."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed at the party."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of hosting the tea party based on tea and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
