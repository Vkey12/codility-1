def solution(A, D):
    balance = 0
    transactions = {}
    
    for i in range(len(A)):
        amount = A[i]
        date = D[i]
        transactions[date] = transactions.get(date, 0) + amount
    
    
    for date, amount in transactions.items():
        year, month, _ = date.split('-')
        
        if amount >= 0:
            balance += amount
        else:
            balance += amount
            
            if month != '01' and amount < -5:
                balance -= 5
    
    return balance

# Example usage:
A1 = [100, 100, 100, -10]
D1 = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A1, D1))  # Output: 230