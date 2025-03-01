""""Wordle!"""

__author__ = "730468679"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    max_turns = 6  # 6 user guesses

    while turns < max_turns:  # loop to prompt each guess and feedback
        turns = turns + 1
        print(f"=== Turn {turns}/6 ===")

        guess = input_guess(len(secret))  # guess acquired
        result = emojified(guess, secret)  # emoji version
        print(result)

        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            return

    print("X/6 - Sorry, try again tomorrow!")


def contains_char(search_string: str, target_char: str) -> bool:
    """Iterates through a string looking for a single target character, if not found, returns False, if found returns True"""
    assert (
        len(target_char) == 1
    ), f"len('{target_char}') is not 1"  # ensures guess is actually 1 character
    index = 0
    while index < len(
        search_string
    ):  # while loop indexes through each character in the string
        if search_string[index] == target_char:
            return True
        index = index + 1
    return False


WHITE_BOX: str = "\U00002B1C"  # emoji for white box
GREEN_BOX: str = "\U0001F7E9"  # emoji for green box
YELLOW_BOX: str = "\U0001F7E8"  # emoji for yellow box


def emojified(guess: str, secret: str) -> str:
    """Compares a guess string to the secret string and displays it using emoji boxes"""
    assert len(guess) == len(
        secret
    ), "Guess must be the same length as secret"  # ensures guess length matches the secret

    index = 0
    result = ""

    while index < len(guess):
        if (
            guess[index] == secret[index]
        ):  # if part of the guess letters align with the secret, green box
            result = result + GREEN_BOX
        elif contains_char(secret, guess[index]):  # right, but wrong spot
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX  # no correct char is found
        index = index + 1

    return result


def input_guess(expected_length: int) -> str:
    """With an input guess of an expected integer length, will prompt for a guess of that length"""
    guess = input(
        f"Enter a {expected_length} character word: "
    )  # prompts the user to guess a word
    while len(guess) != expected_length:
        guess = input(
            f"That wasn't {expected_length} chars! Try again: "
        )  # feedback for when words are of the wrong length

    return guess


if __name__ == "__main__":
    main(secret="codes")
