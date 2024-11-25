TotalAmountBeingRented = 100000
AnnualInterestRate = 0.15
NumberOfPeriodsPerYear = 12
TotalDuration = 3

r = AnnualInterestRate / NumberOfPeriodsPerYear
n = NumberOfPeriodsPerYear * TotalDuration

numerator = (TotalAmountBeingRented * r) * ((1 + r) ** n)
denominator = ((1 + r) ** n) - 1

PMT = numerator / denominator

for i in range(n):
    cost = TotalAmountBeingRented
    Interest = cost * r
    PrincipalRepayment = PMT - Interest
    if PrincipalRepayment > cost :
        RemainingPrincipal = 0
    else:
        RemainingPrincipal = cost - PrincipalRepayment
    TotalAmountBeingRented = RemainingPrincipal
    print(f"{cost:.2f} | {PMT:.2f} | {PrincipalRepayment:.2f} | {RemainingPrincipal:.2f}")
