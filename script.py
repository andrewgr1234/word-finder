text= 
"""
"""
lst = text.splitlines()
print(lst)
mylist = [" ", " " ]
for index in mylist:
    for line in lst:
        if index in line:
            print('The Word :'  , index , "- The Line : " , lst.index(line)+1)
