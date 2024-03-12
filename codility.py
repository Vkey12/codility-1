def solution(A, D):
    balance = 0
    monthly_fees = 5
    cards = {}
    
    # using zip to loop
    for i, date in zip(A, D):
        month = int(date.split('-') [1])
        if i >= 0:
            balance += i
        else:
            # if negative the balance to be updated
            balance += i
            if month in cards:
                cards[month].append(i)
            else:
                cards[month] = [i]
    # loop through months
    for month in range(1, 13):
        if month in cards and len(cards[month]) >= 3 and sum (cards[month]) >= -100:
            balance += monthly_fees * (len(cards[month]) - 3)
        else:
            balance -= monthly_fees
    return balance


# Example 
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))

# year 2020
# balance 0
# amount < 0 === card payment && fee = 5
# amount >= 0 === income transfer
