text= """

"""
lst = text.splitlines()
print(lst)
mylist = [" ", " "]
for index in mylist:
    for line in lst:
        if not index in text:
            print('The Word' , index ,'Was Not Found')
        if index in line:
            print('The Word :'  , index , "- The Line : " , lst.index(line)+1)
