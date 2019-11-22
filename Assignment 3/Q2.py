l = ["Waris",  "3", 4,2,2.3,"world"]
q=[]
for value in l:
    if type(value) == int or type(value) == float:
        q.append(value)
print('Numeric value found in a list :')
for i in q:
    print(i,end=' , ')
