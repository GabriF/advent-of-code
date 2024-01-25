def get_couple(line):
    return tuple(tuple(map(int, x.split('-'))) for x in line.strip().split(','))


def d4p1():
    with open("d04.txt") as inputf:
        tot = 0

        for line in inputf:
            t1, t2 = get_couple(line)
            
            if t2[0] <= t1[0] <= t2[1] and t2[0] <= t1[1] <= t2[1]:
                tot += 1 
            elif t1[0] <= t2[0] <= t1[1] and t1[0] <= t2[1] <= t1[1]:
                tot += 1

        return tot


def d4p2():
    with open("d04.txt") as inputf:
        tot = 0

        for line in inputf:
            t1, t2 = get_couple(line)

            if t2[0] <= t1[0] <= t2[1] or t2[0] <= t1[1] <= t2[1]:
                tot += 1 
            elif t1[0] <= t2[0] <= t1[1] or t1[0] <= t2[1] <= t1[1]:
                tot += 1

        return tot

        
if __name__ == "__main__":
    print(d4p1())
    print(d4p2())