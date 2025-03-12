def track_spending():
    balance = 200
    balances = [balance]

    while balance > 0:
        try:
            transaction = int(input("Enter the amount spent: "))
            if transaction == 0:
                break
            balance -= transaction
            balances.append(balance)
        except ValueError:
            print("That is not a valid transaction.")

    print("My bank balances have been:")
    for b in balances:
        print(b)

if __name__ == "__main__":
    track_spending()