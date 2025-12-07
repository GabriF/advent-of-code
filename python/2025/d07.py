import sys


def search_beam(beams: list[int], beam: int) -> int:
    left = 0
    right = len(beams) - 1

    while left <= right:
        mid = (left + right) // 2
        val = beams[mid]

        if val == beam:
            return mid
        elif val < beam:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def split(beams: list[int], beam: int) -> bool:
    index = search_beam(beams, beam)
    if index == -1:
        return False

    prev_beam = beam - 1
    succ_beam = beam + 1

    beams.pop(index)
    added = 0
    if index == 0 or beams[index - 1] != prev_beam:
        beams.insert(index, prev_beam)
        added += 1

    if index == 0 or index + added == len(beams) or beams[index + added] != succ_beam:
        beams.insert(index + added, succ_beam)

    return True


def path_calculator(pos: int, lines: list[str]) -> int:
    return 1 + _path_calculator_helper(pos, 0, lines, {})


def _path_calculator_helper(pos: int, current_line: int, lines: list[str], mem: dict[tuple[str, str], int]) -> int:
    if current_line == len(lines) - 1:
        return 0

    if (pos, current_line) in mem.keys():
        return mem[(pos, current_line)]

    line = lines[current_line]
    val = line[pos]
    
    if val != "^":
        return _path_calculator_helper(pos, current_line + 1, lines, mem)
    
    tot = 1
    if pos > 0:
        tot += _path_calculator_helper(pos - 1,
                                        current_line + 1, lines, mem)
    if pos < len(lines):
        tot += _path_calculator_helper(pos + 1,
                                        current_line + 1, lines, mem)
    mem[((pos, current_line))] = tot
    return tot
    
        

lines = sys.stdin.read().strip().split("\n")

for i, val in enumerate(lines[0]):
    if val == "S":
        start = i
        break

s_1 = 0
beams = [start]
for line in lines[1:]:
    for i, val in enumerate(line):
        if val == "^":
            if split(beams, i):
                s_1 += 1


s_2 = path_calculator(start, lines)

print((s_1, s_2))
