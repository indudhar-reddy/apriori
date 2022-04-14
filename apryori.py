from apyori import apriori
from flask import render_template

def Apryori(d):
    size=d.shape
    records = []
    for i in range(0, size[0]):
        records.append([str(d.values[i,j]) for j in range(0, size[1])])
    association_rules = apriori(records, min_support=0.0059, min_confidence=0.30, min_lift=3, min_length=2)
    association_results = list(association_rules)
    results = []
    for item in association_results:
        pair = item[0]
        items = [x for x in pair]
        res = "Rule: " + items[0] + " -> " + items[1]
        results.append(res)
        #Support
        #second index of the inner list
        res = str(item[1])
        results.append(res)
        #confidence
        #third index of the list located at 0th
        #of the third index of the inner list
        res =str(item[2][0][2])
        results.append(res)
        #LIFT
        res =str(item[2][0][3])
        results.append(res)
        res = "=>"
        results.append(res)
        
    return render_template('result.html', result=results)