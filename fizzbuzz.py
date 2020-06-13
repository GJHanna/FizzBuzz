
def fizzbuzz(cond, start, end):
    if (start%cond[0]==0 and start%cond[1]==0):
        print('{}: Fizz Buzz'.format(start))
    elif (start%cond[0]==0):
        print('{}: Fizz'.format(start))
    elif (start%cond[1]==0):
        print('{}: Buzz'.format(start))
    if (start == end):
        return
    fizzbuzz(cond, start+1, end)

if __name__ == "__main__":
    cond = [3, 5] # Fizz, Buzz
    fizzbuzz(cond, 1, 100)