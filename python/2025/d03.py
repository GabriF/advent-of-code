import sys


def find_max_digit_sequence(string: str, number_of_digits: int) -> int:
    assert number_of_digits > 0
    assert len(string) >= number_of_digits

    max_sequence = []

    for i in range(number_of_digits):
        string_len = len(string)

        sub_str = string[:string_len - number_of_digits + i + 1]
        max_pos, max_val = max(
            enumerate(sub_str),
            key=lambda x: x[1]
        )

        string = string[max_pos + 1:]
        max_sequence.append(max_val)
    return int("".join(max_sequence))


input_lines = sys.stdin.readlines()

s_1 = sum(find_max_digit_sequence(line, 2) for line in input_lines)
s_2 = sum(find_max_digit_sequence(line, 12) for line in input_lines)

print((s_1, s_2))
