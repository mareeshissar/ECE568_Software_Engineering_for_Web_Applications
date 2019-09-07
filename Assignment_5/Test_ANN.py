
# coding: utf-8

# In[92]:


import numpy as np
learning_rate=float(input('enter the learning rate'))
target_error=float(input('enter the target error'))

def act_funct(x):
    return 1/(1+np.exp(-x))

def slope_act_funct(x):
    return x*(1-x)

x=np.array([[0,0], [0,1], [1,0], [1,1]])
y=np.array([[0],[1],[1],[0]])


w1=2 * np.random.random_sample((2, 2)) - 1
print("Initial weights after input layer:")
print(w1)

w2=2 * np.random.random_sample((2, 1)) - 1
print("Initial weights after hidden layer:")
print(w2)

def ann(w1,w2):
    l1=np.matmul(x,w1)
    l1=act_funct(l1)     #output of the hidden layer after activation
    l2=np.matmul(l1,w2)
    l2=act_funct(l2)     #final output after activation
     

    batch_error=(y-l2)**2     
    batch_error1=(np.sum(batch_error))**0.5
       
    error2=(y-l2)*slope_act_funct(l2)

    
    #updating weights for output layer
    w2=w2+learning_rate*np.matmul(l1.T,error2)
  
    
    a=np.matmul(error2,w2.T)
    l1=slope_act_funct(l1)
    error1=np.multiply(a,l1)
 
    #updating weights for hidden layer
    w1=w1+learning_rate*np.matmul(x.T,error1)

    
    return batch_error1,w1,w2

be,wt1,wt2=ann(w1,w2)
print("First-batch error is:")
print(be)

c=0

while be>=target_error:
    c=c+1
    be,wt1,wt2=ann(wt1,wt2)
    
   
    
print("Final weights after input layer:")
print(wt1)
print("Final weights after hidden layer:")
print(wt2)
print("Final error is:")
print(be) 
print("The total number of batches run through in the training is:")
print(c)  


     
    
   

