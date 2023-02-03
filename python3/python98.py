#!/usr/bin/python3
# vvvv import libs vvvvv  
import math

# ^^^^ import libs ^^^^
  
# vvvv functon def vvvvv  

def triangles(f_t, f_sm):  #it's function def. f_t get value from  tp[i], and f_sm = l_sm 
    lk = f_t["r"]*2/f_t["c"] # it's coefficient k and formula from whicn we counting k
    print("lk=" + str(lk))
    for i in range(f_t["r"]):  #f_t.r it means tp[i].r, the height
        ik=i*lk
        j = round(f_sm - ik-0.5) #j it's a counter of colums
        jn = round(f_sm + ik+0.5)
        print(" i=" + str(i)+ " ik=" + str(ik)+ " j=" + str(j)+ " jn=" + str(jn)) 
        k=0
        while (k <= j):
            print(" ",end='')
            k = k + 1
            
        while (j <= jn):
            print("*",end='')
            j = j + 1
        print("")    
# ^^^^ functon def ^^^^  

# vvvv  main vvvvv  

nt = int(input("enter the count of tiangles: "))
tp = [] # here i announced array
for i in range(0,nt) :
    
    l_tt = {"r":0,"c":0} # it means that
    l_str="enter the height number["+str(i)+"]: "    
    l_tt["r"] = int(input(l_str))
    l_stt="enter the weight number["+str(i)+"]: "  
    l_tt["c"] = int(input(l_stt))
    tp.append(1)
    tp[i] = l_tt

l_change = True # it's a flag, if it means true it means that it will be checking the while condition. so how long it stays true (i meant flag) 
#machine will be checking while  conditions
l_tmp = {}
while l_change:
    l_change = False # here i changed my flag from true to false 
  # after that i sorted the values of triangles 
    for i in range(0,nt-1) :  # i wrote nt-1 cause function range print out diapason between 0 and penultimate number. fpr example if i chose 3 triangles
   # nt will be equal to 3,  but range starts counting from 0 index, so 3 for range it's not a 123, it's 012
         # it was made in advance if user didn't write triangles in an ascending row/line. if second triangle is bigger that third for example
       # so i compared the values of triangles to find out which the bigger 
        if tp[i]["c"] > tp[i+1]["c"]   or (tp[i]["c"] == tp[i+1]["c"] and tp[i]["r"] > tp[i+1]["r"]):
          l_tmp = tp[i]
          tp[i] =   tp[i+1] 
          tp[i+1] = l_tmp
          l_change = True

for i in range(0,nt):
    print("tp["+str(i)+"][c]"+str(tp[i]["c"])+ " tp["+str(i)+"][r]" + str(tp[i]["r"]))


l_sm = round((tp[nt-1]["c"]+1)/2)
print("l_sm= " + str(l_sm))
for i in range(0,nt):
    triangles(f_t=tp[i],f_sm = l_sm)		
# ^^^^ main ^^^^  
