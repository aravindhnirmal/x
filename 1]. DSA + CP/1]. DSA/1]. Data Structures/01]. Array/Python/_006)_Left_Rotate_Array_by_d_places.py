def  left (arr,d):
    for i in range(d) :
        arr .append (arr .pop ( 0 ))
        #append  means add the element in the last of the list
        #pop means delete the element from the list
        #this do for  loop  for  d  times and  first  is do  pop  and  then  append
        # 4  times   na  pop 0   la  irukurathu  and  append  last   le
    print (arr )
 #method 2 print(l[d:]+l[0:d])   as like the left rotate by 1  program  we  use  this  method  also for  left  rotate  by  d  places
arr=[1,2,3,4,5]
d=4
left(arr,d)
