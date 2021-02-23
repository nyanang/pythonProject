# getSalary() 연봉 구하기 연차 * 900만원
# getVAT() 부가가치세 -> money * 0.1
# 내 연봉에 대한 부가가치세가 얼마인지?

def getSalary(year):
    return year*9000000

def getVAT(money):
    return money * 0.1

mySalary = getSalary(7) #6300만원
myVat = getVAT(mySalary) #630만원
print(myVat)

# g o f () -> getVAT o getSalary(7)
print(getVAT(getSalary(7)))