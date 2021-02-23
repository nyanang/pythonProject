message = "{}님 안녕하세요".format("경록")
print(message)

message = "{}님 {} {}".format("경록","hello", 33 )
print(message)

def printMessage(name, greet):
    message = "{}님 {}".format(name, greet)
    print(message)

printMessage("경록", "안녕하세요")
printMessage("미미", "안녕히가세요")
