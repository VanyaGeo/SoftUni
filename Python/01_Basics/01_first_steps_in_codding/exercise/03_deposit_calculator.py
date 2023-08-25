deposit_amount_money=float(input())
deposit_amount_time=int(input())
yearly_rate_percent=float(input())/100
amount_money_from_the_rate=(deposit_amount_money*yearly_rate_percent)/12
result=deposit_amount_money+deposit_amount_time*amount_money_from_the_rate
print(result)
