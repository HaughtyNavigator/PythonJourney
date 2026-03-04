def TOH(N, fromm, to, aux):
    count = 0
    def helper(N, fromm, to, aux):
        nonlocal count
        if N == 1:
            print("disk " + str(N) + " moved from tower "+ str(fromm) + " to tower "+ str(to) + " via tower " + str(aux))
            count+=1
            return
        helper(N-1, fromm, aux, to)
        print("disk " + str(N) + " moved from tower "+ str(fromm) + " to tower "+ str(to) + " via tower " + str(aux))
        count+=1
        helper(N-1, aux, to, fromm)
    helper(N, fromm, to, aux)
    return count

if __name__ == "__main__":
    moves = TOH(3, 1, 3, 2)
    print("Total moves:", moves)

