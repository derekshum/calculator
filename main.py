
def get_number_from_digits(digit_stack: list[int]) -> int:
    digits: int = 0
    current_number: int = 0
    while len(digit_stack) > 0:
        current_number += int(digit_stack.pop()) * 10 ** digits
        digits += 1
    return current_number


def add_or_subtract(digit_stack: list[int], previous_operator_positive: bool) -> int:
    current_number: int = get_number_from_digits(digit_stack)

    if previous_operator_positive:
        return current_number
    else:
        return -current_number


def calculate(s: str) -> int:
    digit_stack: list[int] = []
    previous_operator_positive: bool = True
    total: int = 0
    for c in s:
        if c == ' ':
            pass # 2 3 treated as 23
        elif c.isdigit():
            digit_stack.append(int(c))
        elif c in ['+', '-']:
            if len(digit_stack) > 0:
                total += add_or_subtract(digit_stack, previous_operator_positive)
                if c == '+':
                    previous_operator_positive = True
                else:
                    previous_operator_positive = False
            elif c == '-':
                previous_operator_positive = not previous_operator_positive

    total += add_or_subtract(digit_stack, previous_operator_positive)
    return total


if __name__ == '__main__':
    while True:
        print('Type your equation in and press enter (only +, -, and numbers will be considered currently)')
        equation = input()
        print(calculate(equation))
