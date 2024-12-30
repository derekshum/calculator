
def get_number_from_digits(digit_stack: list[int]) -> int:
    digits: int = 0
    current_number: int = 0
    while len(digit_stack) > 0:
        current_number += int(digit_stack.pop()) * 10 ** digits
        digits += 1
    return current_number


def add_or_subtract(digit_stack: list[int], operator_stack: list[bool], number_stack: list[int], due_to_parenthesis_closing: bool = False):
    if len(digit_stack) > 0:
        current_number: int = get_number_from_digits(digit_stack)
        if operator_stack.pop():
            number_stack[len(number_stack) - 1] += current_number
        else:
            number_stack[len(number_stack) - 1] -= current_number
    elif due_to_parenthesis_closing:
        operator_stack.pop()


def calculate(s: str) -> int | str:
    digit_stack: list[int] = []
    operator_stack: list[bool] = [True] # Operation to do with current parenthesis nesting. True is positive/plus, False is negative/minus
    number_stack: list[int] = [0] # Running total at current parenthesis nesting.
    for c in s:
        if c == ' ':
            pass # 2 3 treated as 23
        elif c.isdigit():
            digit_stack.append(int(c))
        elif c in ['+', '-']:
            if len(digit_stack) > 0:
                add_or_subtract(digit_stack, operator_stack, number_stack)
                if c == '+':
                    operator_stack.append(True)
                else:
                    operator_stack.append(False)
            elif c == '-':
                operator_stack[len(operator_stack) - 1] = not operator_stack[len(operator_stack) - 1]
        elif c == '(':
            operator_stack.append(True)
            number_stack.append(0)
        elif c == ')':
            add_or_subtract(digit_stack, operator_stack, number_stack, True)
            current_operator: bool = operator_stack.pop()
            current_number: int = number_stack.pop()
            if current_operator:
                number_stack[len(number_stack) - 1] += current_number
            else:
                number_stack[len(number_stack) - 1] -= current_number
            operator_stack.append(True)
        else:
            return f'Invalid character {c}'
    add_or_subtract(digit_stack, operator_stack, number_stack)
    return number_stack[0]


if __name__ == '__main__':
    while True:
        print('Type your equation in and press enter. Only +, -, (, ), and numbers will be considered currently.')
        equation = input()
        print(calculate(equation))
