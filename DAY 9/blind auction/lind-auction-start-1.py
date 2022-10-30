# Show logo from art.py
import art
print(art)
bid_dic = {}
start_bid = True
while start_bid:
    name = input("What is your name: ")
    bid_price = int(input("What is your bid in $"))
    bid_dic[name] = bid_price
    other_bidders = input("Does anyone else want  to bid, Y for Yes N for No").lower()
    if other_bidders == "y":
        start_bid = True
    elif other_bidders == "n":
        start_bid = False
    else:
        print("Wrong input")
        other_bidders = input("Does anyone else want  to bid, Y for Yes N for No").lower()
        start_bid = True
check = 0
who = ""
for key in bid_dic:
    value = (bid_dic[key])
    if value > check:
        check = value
        who = key


print(f"You won with ${check} and name is {who}")
print(bid_dic)
