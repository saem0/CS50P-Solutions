due = 50

print(f"Amount Due: {due}")

while True:
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        due -= coin

    if due <= 0:
        break
    else:
        print(f"Amount Due: {due}")
        continue

owed = abs(due)
print(f"Change Owed: {owed}")
