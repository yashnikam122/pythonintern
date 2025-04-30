list1=[60,40,10,70]
'''
if not list1:
print(" list is empty:-",list1)
else:
     print("list minimum value is:-",min(list1))
     print("list maximun value is:-",max(list1))

     '''
def minmax_List(list1):
     for i in range(0,len(list1)-1):
          for j in range(i+1,len(list1-1)):
               if( list1[i]>list1[j]):
                    temp=list1[i]
                    list1[i]=list1[j]
                    list1[j]=temp
                    return list1[-1],list1[0]

minvalue=minmax_List(list1)