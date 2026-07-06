merchant_id = "10001"
merchant_name = "Abbas bagh"
is_active = True
fee_rate = .015
location = ("tehran","iran")
last_error = None
amounts = [100000,250000,150000,258000]
channels = {'pos','IPG',"Mobile"}

merchant = {"id": merchant_id,"merchant_nme":merchant_name,"is_active":is_active,"fee_rate":fee_rate,"location":location,"lasterror":last_error,
            "amounts":amounts,"channels":channels}
totalamount = sum(amounts)
transaction_count = len(amounts)
# print(totalamount,transaction_count)
average_amount = totalamount/transaction_count
print(average_amount)
# city = merchant
# country = merchant[location]
print(merchant["amounts"][0])
merchant["amounts"].append(90000)
print((merchant["amounts"]))
print(f"Merchant Name: {merchant['merchant_nme']}")


