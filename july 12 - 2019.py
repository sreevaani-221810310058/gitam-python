#!/usr/bin/env python
# coding: utf-8

# In[4]:


#function to test two digit number matching
import re
def twoDigitMatching(n):
    pattern='^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12))#true
print(twoDigitMatching(123))#false


# In[5]:


#function to define to test username having 8 characters
#upper case and lower case
def testUsername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# ### REGULAR EXPRESSIONS FOR CHARACTERS
# - [A-Z]----FOR UPPER CASE
# -[a-z]-----FOR LOWER CASE
# - [a-zA-Z]----combination of upper and lower char
# -[a-zA-Z0-9]-----combination of upper and lower case char along with no.
# 

# ### regular expression to match the indian mobile number
# - 10 digits
# -(first digitwill be [6-9]) and remaining 9 digits will be[0-9]
# -eg--9848346482
# -re---^[6-9][0-9]{9}$
# -re---^[+][9][1][6-9][0-9]{9}

# In[8]:


#FUNCTION TO VALIDATE THE INDIAN MOBILE NUMBER
def phoneNumberValidation(phone):
    pattern='^[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
phoneNumberValidation('+919848452356')


# - regular expression to validate roll number
#   - example : 1521A0501
#               1521A0109
#               1521A0499
#   -regular expression to validate password
#    - parameters : Len min of 6 characters and Max of 15 characters
#    - accept lower case,uppercase,digitspecialchar(@,#,!)
#    

# ### email id validation using regular expression
# -example : username@domainname.extension
# -username :-
#       - length will be [6-15]
#       - no spls characters apart from underscore(_)
#       - should not begin and ends with underscore
#       -characters set: all digits and lower case
# -domain name :
#        - length will b e [3-18]
#        -no  spsls characters
#        -character set : all digits and lowercase
# -extension :
#      - length will be [2-4]
#      - no spls char
#      - character set: lower case char
#  
# 

# In[11]:


def emailIdValidation(email):
    pattern='^[0-9a-z][0-9a-z_.]{5,14}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailIdValidation('sreevijkid@gmail.com')
    
    


# ### python turtle
#   - turtle graphics

# In[1]:


#step 1: make all the turtle package to be imported
import turtle
#turtle method creates and returns a new object
a1=turtle.Turtle()
#forward() method moves 100 pixels
turtle.forward(250)
#we are done 
turtle.done()


# In[3]:


import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[5]:


#draw square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[1]:


#draw square
import turtle as tt
a1=tt.Turtle()
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
tt.done()


# In[5]:


#loop statement
import turtle as tt
a1=tt.Turtle()
for i in range(4):
    a1.backward(150)
    a1.left(90)
tt.done()


# In[7]:


#star
import turtle as t
a1 = t.Turtle()
for i in range(40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[ ]:


#spiraling star
import turtle as t
a1 = t.Turtle()
a1.pencolor('pink')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:


#square spiral
import turtle as t
a1 = t.Turtle()
a1.pencolor('orange')
for i in range(250):
    a1.forward(i)
    a1.right(91)
t.done()


# In[1]:


#hexagon with multicolour
from turtle import *
colors = ['blue','green','yellow','orange','purple','black']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100 + 1)
    forward(x)
    left(59)
    


# In[3]:


#goto function
from turtle import *
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[ ]:


#setheading(heading)
#will change the current direction to heading angle
from turtle import *
colors = ['blue','red','yellow','purple','pink','orange']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write(str(angle)+'0')
    backward(100)


# In[6]:


from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90):
    undo()


# In[4]:


from turtle import *
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)


# In[1]:


from turtle import *
pensize(50)
pencolor('blue')
forward(250)
pencolor(0,1.0,0)
forward(250)
pensize(10)
goto(-400,50)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red/4.0,green/4.0,blue/4.0)
            forward(10)


# In[ ]:


#draw rectangle
import turtle as tt
a1=tt.Turtle()
a1.backward(350)
a1.left(90)
a1.forward(150)
a1.left(90)
a1.backward(350)
a1.left(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[1]:


from turtle  import *
colors = ['purple' , 'green' , 'blue' , 'orange' , 'pink' , 'red']
reset()
up()
goto(-320,-195)
width(90)
for pcolor in colors:
    color(pcolor)
    down()
    forward(750)
    up()
    backward(750)
    left(90)
    forward(100)
    right(90)
width(55)
color('white')
goto(0,-170)
down()

circle(170)
left(90)
forward(340)
up()
left(180)
forward(170)
up()
backward(170)
left(90)
down()
forward(170)
up()
goto(0,300)


# In[ ]:




