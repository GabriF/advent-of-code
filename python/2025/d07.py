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


lines = sys.stdin.read().split("\n")

beams = []
for i, val in enumerate(lines[0]):
    if val == "S":
        beams.append(i)

s_1 = 0
for line in lines[1:]:
    for i, val in enumerate(line):
        if val == "^":
            if split(beams, i):
                s_1 += 1

print(s_1)
