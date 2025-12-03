import sys
    

def find_max_digit_sequence(string : str, sequence_len : int) -> int:
    assert sequence_len > 0
    assert len(string) >= sequence_len
    max_sequence = [0] * sequence_len
    string_list = [c for c in string.strip()]
    for i in range(sequence_len):
        string_list_len = len(string_list)
        max_pos, max_val = max(
            enumerate(string_list[:string_list_len - sequence_len + i + 1]),
            key=lambda x: x[1]
        )
        string_list = string_list[max_pos + 1:]
        max_sequence[i] = max_val
    return int("".join(max_sequence))

input_lines = sys.stdin.readlines()
s_1 = sum(find_max_digit_sequence(line, 2) for line in input_lines)
s_2 = sum(find_max_digit_sequence(line, 12) for line in input_lines)
print((s_1, s_2))
