def bisection_fixed_payment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPaymentLower = balance / 12.0
    monthlyPaymentUpper = (balance * (1 + monthlyInterestRate)**12) / 12.0
    fixedPay = (monthlyPaymentUpper + monthlyPaymentLower) / 2

    while (monthlyPaymentLower < (monthlyPaymentUpper - 0.001)):
        fixedPay = (monthlyPaymentUpper + monthlyPaymentLower) / 2
        debt = balance
        for month in range(12):
            debt = debt - fixedPay
            debt = debt * (1 + monthlyInterestRate)
        if debt <= 0:
            monthlyPaymentUpper = fixedPay
        else:
            monthlyPaymentLower = fixedPay
    print "Lowest Payment: %.2f" % fixedPay


bisection_fixed_payment(balance=320000, annualInterestRate=0.2)
