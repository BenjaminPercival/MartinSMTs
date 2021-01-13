#!/usr/bin/env python
# coding: utf-8

# In[4]:


from z3 import *


v = [Int('v%s' % (i)) for i in range(64)] #4 x 16 entries of vector bundle vecs

s=Solver() #z3 solver initiated

#impose a range on entries which are in Z/4 really but we multiply by 4 so equal 1,2,3 or 4
range1  = [ And(1 <= v[i], v[i] <= 4) for i in range(64)]
s.add(range1)

#define the entries of the inner product matrix
V1_00= sum([v[i]*v[i] for i in range(16)])
V1_01= sum([v[i]*v[i] for i in range(16,32)])
V1_10= sum([v[i]*v[i] for i in range(32,48)])
V1_11= sum([v[i]*v[i] for i in range(48,64)])

s.add(V1_00+V1_01+V1_10+V1_11==96) # toy version of simplest Bianchi identity

print(s.check()) #checks satisfiability of constraints
countr=0 
while s.check() == sat: #enumerates solutions
    m = s.model ()
    countr+=1
    if not m:
        break
    #f = open('ToyMartin.txt','a')
    #old_stdout = sys.stdout  #  store the default system handler to be able to restore it
    #sys.stdout = f
    print("solution", countr)
    print("v1:", [m[v[i]] for i in range(16)]) #could divide 4 here probably
    print("v2:", [m[v[i]] for i in range(16,32)])
    print("v3:", [m[v[i]] for i in range(32,48)])
    print("v4:", [m[v[i]] for i in range(48,64)])
    #print(sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0])))
    #print(sorted ([(m[d]) for d in m], key = lambda x: str(x[0])))
    #f.close()
    #sys.stdout=old_stdout
    
    s.add(Not(And([v() == m[v] for v in m]))) #ignores solutions already found



# In[ ]:




