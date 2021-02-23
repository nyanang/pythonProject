val1 = 1 #숫자
print(val1)

val2 = "1" #문자열
print(val2)형

print(val1+20) #21
#print(val2+20) #21? 에러

print(type(val2))

print(int(val2)+30)

#숫자형을 문자열로
print(val2 + str(20)) #120

result = val2 + str(20)
print(result, type(result))
print(result + "40") #12040
print(int(result) + 40) #160
