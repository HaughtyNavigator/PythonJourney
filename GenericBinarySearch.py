tests = []
#Add further test cases as necessary, this was just a demo for a question I faced:
#Find the starting index and ending index of a specified number in a sorted ascending order list

tests.append({
    'input':{
        'array': [1,1,2,2,2,3,4,5],
        'query': 2
    },
    'output': [2,4]
})

#Defining a binary search function which could be reused later
def binary_search(start, end, condition):
    while(start <= end):
        mid = (start + end) // 2
        res = condition(mid)
        if(res == 'left'):
            end = mid-1
        elif(res == 'found'):
            return mid
        else:
            start = mid + 1

    return -1

#Finding the first occurence of the number in the list
def find_first(array, query):
    def condition(mid):
        if(query == array[mid]):
            if(mid-1 >= 0 and array[mid-1] == query):
                return 'left'
            else:
                return 'found'
        elif(query < array[mid]):
            return 'left'
        else:
            return 'right'
        
    return binary_search(0, len(array)-1, condition)

#Finding the last occurence of the number in the list
def find_last(array, query):
    def condition(mid):
        if(query == array[mid]):
            if(mid+1 <= len(array)-1 and array[mid+1] == query):
                return 'right'
            else:
                return 'found'
        elif(query > array[mid]):
            return 'right'
        else:
            return 'left'
        
    return binary_search(0, len(array)-1, condition)

#Iterating through the tests and checking whether we got the cases right or wrong.
for test in tests:
    results = []
    results.append(find_first(**test['input']))
    results.append(find_last(**test['input']))
    print(results == test['output'])

#Complexity of the code in 2*log(N) == log(N)
