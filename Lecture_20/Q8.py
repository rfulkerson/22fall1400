def coins(total):
    total = int(total * 100)
    q = total // 25
    total %= 25
    d = total // 10
    total %= 10
    n = total // 5
    p = total % 5
    return [q, d, n, p]


money = float(input("Enter amount: "))
qu, di, ni, pe = coins(money)
print(qu, di, ni, pe)