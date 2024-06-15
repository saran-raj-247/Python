def computesalary(basic):
    da=int(basic*0.4)
    ha=int(basic*0.2)
    gross=da+basic+ha
    return gross
basic=int(input())
print(computesalary(basic));
