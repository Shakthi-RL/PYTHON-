arr=list(map(int,input().split()))
#this is for arr storing
count_arr=[0]*((max(arr))+1)
for num in arr:
    count_arr[num]+=1
print(count_arr)
#this is for dictionary
count_dic={}
for num in arr:
    if num in count_dic:
        count_dic[num]+=1
    else:
        count_dic[num]=1
print(count_dic)
