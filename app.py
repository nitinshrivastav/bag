#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data=pd.read_csv("50_Startups.csv")


# In[4]:


x=data.iloc[:,0:-2]
y=data.iloc[:,-1]


# In[5]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20)


# In[6]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()


# In[7]:


model.fit(xtrain,ytrain)


# In[10]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def nitin():
    return render_template('sneha.html')
@app.route('/info',methods=['GET','POST'])
def fkjfkjf():
    if(request.method=='POST'):
        res=int(request.form['r'])
        admin=int(request.form['a'])
        mark=int(request.form['m'])
        total=model.predict([[res,admin,mark]])
        return render_template('sneha.html',nitin=total) 
if __name__=='__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




