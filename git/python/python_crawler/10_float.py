#float 부동소숫점

val1 = 0.1
val2 = 0.2

print(type(val1), type(val2)) #소수점 float
print(type(1), type(2)) #정수 integer

def divide(val1, val2):
    print(type(val1), type(val2))
    result = val1/val2
    print(result, type(result))

divide(10,20)

