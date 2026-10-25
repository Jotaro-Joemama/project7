import random

print("Dice Roller")
print("Examples: d6, d20 +3, d20 -2, d20 x2")

while True:
    user_input = input("\nEnter your roll (or type 'quit'): ").lower().replace(" ", "")

    if user_input == "quit":
        break

    try:
        # Find the dice type
        d_position = user_input.index("d")

        dice_amount = int(user_input[:d_position]) if d_position > 0 else 1
        sides_end = d_position + 1

        # Find where the dice number ends
        while sides_end < len(user_input) and user_input[sides_end].isdigit():
            sides_end += 1

        dice_sides = int(user_input[d_position + 1:sides_end])

        # Roll the dice
        total = sum(random.randint(1, dice_sides) for _ in range(dice_amount))

        print(f"Roll: {total}")

        # Handle modifiers
        modifiers = user_input[sides_end:]

        while modifiers:
            if modifiers[0] in "+-":
                operator = modifiers[0]
                modifiers = modifiers[1:]

                number_end = 0
                while number_end < len(modifiers) and modifiers[number_end].isdigit():
                    number_end += 1

                number = int(modifiers[:number_end])

                if operator == "+":
                    total += number
                else:
                    total -= number

                modifiers = modifiers[number_end:]

            elif modifiers[0] == "x":
                modifiers = modifiers[1:]

                number_end = 0
                while number_end < len(modifiers) and modifiers[number_end].isdigit():
                    number_end += 1

                number = int(modifiers[:number_end])
                total *= number

                modifiers = modifiers[number_end:]

            else:
                raise ValueError

        print(f"Final result: {total}")

    except (ValueError, IndexError):
        print("Invalid input! Try something like d20 +3 or d6 x2.")