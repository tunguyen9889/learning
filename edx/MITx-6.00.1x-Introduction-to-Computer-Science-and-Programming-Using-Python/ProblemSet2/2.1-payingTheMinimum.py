def credit_card_payment(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    totalPay = 0

    for month in range(1, 13):
        minMonthlyPay = monthlyPaymentRate * balance
        totalPay += minMonthlyPay
        balance = balance - minMonthlyPay
        balance = balance * (1 + monthlyInterestRate)

        print 'Month: ' + str(month)
        print 'Minimum monthly payment: %.2f' % minMonthlyPay
        print 'Remaining balance: %.2f' % balance

    print 'Total paid: %.2f' % totalPay
    print 'Remaining balance: %.2f' % balance

# credit_card_payment(balance, annualInterestRate, monthlyPaymentRate)
credit_card_payment(4213, 0.2, 0.04)
