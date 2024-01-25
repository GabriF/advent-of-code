def readelve(f):
    """
    Reads one elve backpack and return a list of strings. 
    
    f: input file
    """
    t = []
    for line in f:
        l_strip = line.strip()
        if l_strip:
            t.append(l_strip)
        else:
            return t


def move_to_right(l, s = 0):
    """"
    move l one time right, but fixing l[:s + 1]
    """
    if s == len(l) - 1:
        return l
    elif s == 0:
        return [l[-1]] + l[:-1]
    else:
        return l[:s + 1] + move_to_right(l[s + 1:])
    


def d1p1():
    with open("d01.txt") as inputf:
        max = -1
        e = readelve(inputf)
        while e:
            e_sum = sum([int(x) for x in e])
            if e_sum > max:
                max = e_sum
            e = readelve(inputf)
        
        return max
  


def d1p2():
    with open("d01.txt") as inputf:
        top3_elves = [0] * 3
        e = readelve(inputf)
        while e:
            e_sum = sum([int(x) for x in e])

            for i, v in enumerate(top3_elves):
                if e_sum > v:
                    top3_elves = move_to_right(top3_elves, i)
                    top3_elves[i] = e_sum
                    break

            e = readelve(inputf)

        return sum(top3_elves)
            


if __name__ == "__main__":
    print(d1p1())
    print(d1p2())