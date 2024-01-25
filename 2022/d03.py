def get_priority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1


def d3p1():
    with open("d03.txt") as inputf:
        t = 0

        for line in inputf:
            c1 = set(line.strip()[0:len(line) // 2])
            c2 = set(line.strip()[len(line) // 2:])
            common = "".join(c1.intersection(c2))
            t += get_priority(common)

    return t


def d3p2():
    with open("d03.txt") as inputf:
        t = 0

        lines = inputf.readlines()

        for i in range(0, len(lines), 3):
            g = [set(x.strip()) for x in lines[i:i+3]]
            common = "".join(set.intersection(*g))
            t += get_priority(str(common))

    return t


if __name__ == "__main__":
    print(d3p1())
    print(d3p2())
