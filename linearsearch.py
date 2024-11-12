a = [1,2,4,1,685,456,60,61,6,1,5631,864,1,5,16,841,651,68196,1,61,68489,5445]
item = 2
def LinearSearch(array,item):
    for c in array:
        if c == item:
            print(str(item)+" is in the array")
            return
    print(str(item)+" is not in the array")

LinearSearch(a,item)