def By_key(d,reverse=False):
    return dict(sorted(d.items(),key=lambda k:k[0],reverse=reverse))
d={1:2,2:3,4:0,5:7,8:4}
print("Sorted in ascending order:",By_key((d)))
print("sorted in descending order:",By_key(d,True)) 
