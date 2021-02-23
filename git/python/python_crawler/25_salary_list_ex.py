#연봉 = 연차 * 900만원
def getSalary(year):
    return year*9_000_000

years= [7, 3, 4, 6] #=> 63, 27, 36, 54

def getResult(years):
    salaryList = []
    for year in years:
        salary = getSalary(year)
        salaryList.append(salary)
    return salaryList
    print(salaryList)


result = getResult(years)
print("result", result)