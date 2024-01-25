# A = X = Rock
# B = Y = Paper
# C = Z = Scissors
convert_dic = {"X": "A", "Y" : "B", "Z" : "C"}
points_dic = {"A" : 1, "B" : 2, "C" : 3}
cases = {
    ("A", "B") : False,
    ("A", "C") : True,
    ("B", "A") : True,
    ("B", "C") : False,
    ("C", "A") : False,
    ("C", "B"): True
}


def d2p1():
    points = 0
    with open("d02.txt") as inputf:
        for line in inputf:
            l = line.split()
            mine, opponent = convert_dic[l[1]], l[0]

            points += points_dic[mine]
            if mine == opponent:
                points += 3
            elif cases[(mine, opponent)]:
                points += 6
    
    return points


def d2p2():
    # X = Lose
    # Y = Draw
    # Z = Win
    points = 0
    with open("d02.txt") as inputf:
        for line in inputf:
            l = line.split()
            mine, opponent = l[1], l[0]
            if mine == "Y":
                points += 3 + points_dic[opponent]
            elif mine == "X":
                for case in cases:
                    if cases[case] and (case[0] == opponent):
                        points += points_dic[case[1]]
            elif mine == "Z":
                for case in cases:
                    if (not cases[case]) and case[0] == opponent:
                        points += 6 + points_dic[case[1]]


    return points


if __name__ == "__main__":
    print(d2p1())
    print(d2p2())