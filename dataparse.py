import csv
from os import makedirs,getcwd

cwd = getcwd()


def shareinfo(Companyname, broker):
    buy_val = 0
    sell_val = 0
    sumof = 0
    with open(f'{date}.csv', 'r') as tdata:
        value = csv.DictReader(tdata)
        for line in value:
            bank1 = line['Symbol']
            buy_broker = line['Buyer']
            sell_broke = line['Seller']
            quantity_ = line["Quantity"]
            quantity = int(quantity_.replace(",", ""))
            if bank1 == Companyname:
                if buy_broker == broker:
                    buy_val += quantity
                if sell_broke == broker:
                    sell_val += quantity
                sumof = buy_val+sell_val
                # rate_today=rate
                chalkhel='#####' if sumof > 10000 else ""
    return Companyname, broker, buy_val, sell_val,sumof, chalkhel


#part to edit 
company = input('enter company symbol\n')
inp=input('date\n').split()
datelist= list(inp)
makedirs(company)

for i in range(len(datelist)):
    date = datelist[i]
    beingprocessed = []
    appendthis = ('Companyname', 'Brokerno', 'Bought',
                  'sold', 'Totalkitta', '<10k/day')
    beingprocessed.append(appendthis)
    for brokernumber in range(1, 60):
        beingprocessed.append(shareinfo(Companyname=company, broker=str(brokernumber)))
        with open(f'{company}/{company}{date}.csv', 'w') as processeddata:
            csvwriter = csv.writer(processeddata, delimiter='\n')
            csvwriter.writerow(beingprocessed)
