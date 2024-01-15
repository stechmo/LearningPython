import re

transactions=list()

def addtransaction(pdate, pamount, ptype):
    transaction = {"date":pdate,"amount":pamount,"type":ptype}
    transactions.append(transaction)

def findall(my_key,my_value):
    values = [transaction for transaction in transactions if transaction[my_key]==my_value]
    return values

def is_valid_date_format(date_string):
    date_regex = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    match = re.match(date_regex, date_string)
    return bool(match)

addtransaction("10-05-2000",100,"sell")
addtransaction("10-05-2000",14,"sell")

my_date = transactions[0]["date"]
print(is_valid_date_format(my_date))

