import operator
def most_frequent(s):
    d=dict()
    for key in s:
        if key in d:
            d[key]+=1
        else:
            d[key]=1
    sort_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    for key, value in sort_d.items():
        print(key,' =',value)
s="Mississippi"
most_frequent(s)
