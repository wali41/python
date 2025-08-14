
def denomination(amount, denominations):

    for denom in denominations:

        count = amount // denom

        print(f"Notes of {denom} = {count}")

        amount %= denom 

    return amount

denominations_list = [500, 100, 50, 20, 10]

amt = denomination(1230, denominations_list)

print("Remaining amount after denomination:", amt)




