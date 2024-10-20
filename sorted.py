A = [1,2,3,4,5,6,7,9,11,13,6]

for index,num in enumerate(A):
    try:
        if num > A[index +1 ]:
            print("Not sorted")
    except: pass #out of range