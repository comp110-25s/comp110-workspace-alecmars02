"""My first exercise in CAMP110"""

__author__ = "730468679"


def greet(name: str) -> str:
    """A welcoming first function definition"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
