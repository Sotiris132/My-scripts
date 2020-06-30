a = [291, 80, 43, 226, 206, 204, 36, 112, 17, 137, 284, 298, 133, 300, 38, 107, 299, 183, 8, 152, 56, 217, 179, 110, 61, 73, 232, 228, 221, 119, 285, 202, 192, 
     195, 57, 225, 239, 86, 66, 247, 144, 58, 91, 120, 169, 41, 82, 2, 76, 173, 39, 102, 234, 34, 97, 29, 264, 159, 10, 65, 109, 68, 191, 171, 213, 15, 210, 16, 
     209, 50, 111, 178, 3, 49, 260, 62, 263, 242, 261, 227, 31, 168, 200, 219, 128, 193, 254, 160, 24, 129, 170, 12, 106, 187, 166, 124, 126, 81, 79, 296]

#repeating loop len(a)(number of elements) number of times
for j in range(len(a)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1] = a[i+1],a[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print (a)

