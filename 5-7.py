import json
firm_dict = {}
average_profit = []
with open('doc.txt', encoding='utf-8') as doc:
    lines = doc.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('doc.json', 'w') as doc_json:
    json.dump(out_info, doc_json)

with open('doc.json') as doc_json:
    print(json.load(doc_json))
