def calculate_status(totalamount):
    if totalamount >= 1000000 :
        return "High Volume"
    if totalamount < 500000 :
        return "Low Volume"
    else :
        return "Medium Volume"

#print(calculate_status(700000))
try : 
 Tr_count= int(input("How many transactions do you want to enter? "))
 if(Tr_count>0) :
  totalamount =0
  for i in range(1,Tr_count+1):
       while True :
        try :
         amount = int(input(f"Enter amount for transaction {i}: "))
         if amount<=0 :
            print("Invalid amount, try again")
            continue
         totalamount += amount
         break
        except ValueError :
          print("Invalid amount. Try again")
 
  averageamount = totalamount/Tr_count
  print(f"Transaction Count : {Tr_count}")
  print(f"Total amount : {totalamount}")
  print(f"Average Amount : {averageamount}")
  print(calculate_status(totalamount))
 else :
    print("You should have at least one Transaction")
except ValueError :
   print("Invalid Number, try again")