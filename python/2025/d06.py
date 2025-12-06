import sys
import re


def get_problems(raw_input: str) -> tuple[list[int], list[str]]:
    grid_input = [re.split(" +", line.strip()) for line in raw_input]

    problem_operands_number = len(grid_input) - 1
    problem_number = len(grid_input[0])
    print(grid_input)
    operands = [
        [int(grid_input[row][col]) for row in range(problem_operands_number)]
        for col in range(problem_number)
    ]
    function_list = grid_input[problem_operands_number]
    return operands, function_list


def calc(operands: list[int], function: str) -> int:
    operation = {
        "+": lambda op1, op2: op1 + op2,
        "*": lambda op1, op2: op1 * op2
    }[function]
    r = operands[0]
    for op in operands[1:]:
        r = operation(r, op)
    return r


def main():
    raw_input = sys.stdin.readlines()
    operands_list, function_list = get_problems(raw_input)
    s_1 = sum(
        calc(operands, function)
        for operands, function in zip(operands_list, function_list)
    )
    print(s_1)


if __name__ == "__main__":
    main()
