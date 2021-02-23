names = ["kyeongrok", "mimi", "nana", "mingming", "ruru"]

for name in names:
    print(name)

#printHello(name)
def printHello(name):
    message = "{} bye!".format(name)
    print(message)

for name in names:
    printHello(name) #kyeongrok