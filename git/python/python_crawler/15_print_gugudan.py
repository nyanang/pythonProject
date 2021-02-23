# 2단 출력
print("2 * 1 = 2")

# 2단 출력하는 함수

def print2Dan():
    for num in range(1, 9+1):
        print(2, "*", num, "=", 2*num)

print2Dan()


# 3단 출력하는 함수
def print3Dan():
    for num in range(1, 9 + 1):
        print(3, "*", num, "=", 3 * num)

print3Dan()

def printGugudan():
    for num1 in range(1, 9 + 1):
        for num2 in range(1, 9+1):
            print(num1, "*", num2, "=", num1 * num2)

printGugudan()