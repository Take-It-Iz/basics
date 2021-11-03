#summary to basic python grammar
# global variables section
slayerTestament = 'IN THE FIRST AGE, IN THE FIRST BATTLE...ONE STOOD'
multidimensional_array = [
    [1, 2, 3, 4, 5],
    ['somebody', 'once', 'told', 'me'],
    ['the', 'world', 'is', 'gonna', 'roll', 'me']
]
loopStartValue = 0
loopEndValue = 5


# functions section
def testaments_printer(testamentText): #print string
    print(testamentText)
    

def cube(n): #cubic value of a given number with type check
    if n == 0: 
        return 0
    elif isinstance(n, str):
        print('The given argument ' + n + ' is a string. Please, send a numerical argument instead')
    elif (n != 0) and not (n >= 5):
        return n*n*n
    else:
        return 'n*n*n'

def math_power_implementation(value, power): #get power of a given value
    result = 1
    for index in range(power):
        result = result * value
    return result


# loops section
while loopStartValue <= loopEndValue: #print iteration number with every cycle
    print(loopStartValue)
    loopStartValue += 1

for loopStartValue in range(2, 8): #same exvept iterator values areb't global variables 
    print(loopStartValue)
    loopStartValue += 1


# functions calls section
testaments_printer(slayerTestament)

print(cube(3))
print(cube(21))
print(cube('qwerty'))
print(math_power_implementation(3, 5))

print(multidimensional_array[1])
print(multidimensional_array[1][0])