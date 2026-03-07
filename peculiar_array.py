## A peculiar array is a type of an array where each element can either be an integer or a peculiar array itself. We need to return the sum of all the elements within the peculiar array. Each nested peculiar arrays sum is computed
## like this, the elements would be added and raised to the power of how deep it has been nested. Example: [1,2,[3,4],[[2]]], here, 3+4 would be raised to the power 2, and the last element 2 would be raised first to the power of 3
## and then raised to the power of 2.

def sumPow(arr, p):
    sum = 0
    for i in arr:
        if type(i) == int:
            sum+=i
        else:
            sum = sum + sumPow(i, p+1)
    return (sum)**p

if __name__ == "__main__":
    testarr = [1,2,[3,4],[[2]]]
    sum = sumPow(testarr, 1)
    print(sum)
    
