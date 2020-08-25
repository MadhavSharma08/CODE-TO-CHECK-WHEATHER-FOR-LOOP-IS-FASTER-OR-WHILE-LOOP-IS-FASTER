import time 
initial = time.time()
print(initial)
k = 0
while(k<2):
    print("HELLO WORLD")
    k+=1
print("While loop ran in" , time.time() - initial)
initial2 = time.time()
for i in range(2):
    print("HELLO WORLD")
    print("For loop ran in" , time.time()-initial2)