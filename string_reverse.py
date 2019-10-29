lt= raw_input("Enter string: ")
lst=[i for i in lt]
result=[]
begin = 0 
end = len(lst) - 1
while(begin < end): 
    temp = lst[begin] 
    lst[begin] = lst[end] 
    lst[end] = temp
    begin += 1 
    end -= 1 
lsk=''.join(lst)
print(lsk)
