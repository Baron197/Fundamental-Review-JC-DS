def filterDuplikat(fn, collection) :
    newCollection = []
    for item in collection :
        if(fn(item)) :
            newCollection.append(item)
    
    return newCollection

list1 = [1,2,3,4,5]

def angkaGenap(angka) :
    return angka % 2 == 0

newList = filterDuplikat(angkaGenap,list1)
print(newList)
# [2, 4]

print(filterDuplikat(lambda angka: angka % 2 == 0, list1))
# [2, 4]