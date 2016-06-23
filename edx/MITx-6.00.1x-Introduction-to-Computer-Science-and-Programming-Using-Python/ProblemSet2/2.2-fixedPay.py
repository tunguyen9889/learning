def fixed_payment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    fixedPay = balance / 120 * 10
    debt = balance
    while debt > 0:
        debt = balance
        for month in range(1, 13):
            debt -= fixedPay
            if debt <= 0:
                return fixedPay
            debt *= (monthlyInterestRate + 1)
        fixedPay += 10


print "Lowest Payment: " + str(fixed_payment(3329, 0.2))
# print "Lowest Payment: " + str(fixed_payment(balance, annualInterestRate))
