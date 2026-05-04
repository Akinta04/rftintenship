data = [10,None,20,10,"",30,None,40]
clean_list = []
removed_count = 0
for i in data :
    #remove invalid values
    if i is None or i =="":
        removed_count+=1
        continue
    #remove duplicates
    if i not in clean_list:
        clean_list.append(i)
    else:
        removed_count +=1
#sort final_list
clean_list.sort()
print("clean list:",clean_list)
print("removed values count:",removed_count)