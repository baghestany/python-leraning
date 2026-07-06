name = "Abbas"
age = 53
transaction_count = 1200
failed_count = 35

print(f"User : {name}")
print(f"Transaction Count : {transaction_count}")
print(f"Failed transactions : {failed_count}")
if failed_count > 0:
    print("There are Failed Transaction.")
else:
    print("All Transactions are  successful.")
