#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
points=0

def welcome():
    global points
    points+=5
    return f"""
    *****congratulation*****
        You got 5 points
    Now you have {points}points
    ************************"""

def detect():
    global points
    points-=5
    return f"""
    xxxxxxxxxxxxxxxxxxxxxxxx
    *****Wrong Answer*******
     You have lost 5 points
    Now you have {points} points
    ************************"""
    
    
while True:
    
     #lavel 1
    if points<100:
        if points==0:
            print("level 1")
        num1=random.randint(1,10)
        num2=random.randint(1,10)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2)]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
            #lavel 2
    if 10<=points<20:
        if points==10:
            print("lavel 2")
        num1=random.randint(10,50)
        num2=random.randint(10,50)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 1""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
        
         #lavel 3
    if 20<=points<30:
        if points==20:
            print("lavel 3")
        num1=random.randint(50,100)
        num2=random.randint(50,100)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 2""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
    
    #lavel 4
    if 30<=points<40:
        if points==30:
            print("lavel 4")
        num1=random.randint(3,50)
        num2=random.randint(5,70)
             #  ("question"  ,  "answer")
        question=[(f"{num1}*{num2}",num1*num2),
                  (f"{num1}//{num2}",num1//num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 3""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 5
    if 40<=points<50:
        if points==40:
            print("lavel 5")
        num1=random.randint(3,50)
        num2=random.randint(5,70)
             #  ("question"  ,  "answer")
        question=[(f"{num1}*{num2}",num1*num2),
                  (f"{num1}//{num2}",num1//num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 4""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 6
    if 50<=points<60:
        if points==50:
            print("lavel 6")
        num1=random.randint(50,100)
        num2=random.randint(50,100)
             #  ("question"  ,  "answer")
        question=[(f"{num1}*{num2}",num1*num2),
                  (f"{num1}//{num2}",num1//num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 5""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 7
    if 60<=points<70:
        if points==60:
            print("lavel 7")
        num1=random.randint(100,500)
        num2=random.randint(100,500)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2),
                  (f"{num1}*{num2}",num1*num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 6""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 8
    if 70<=points<80:
        if points==70:
            print("lavel 8")
        num1=random.randint(100,500)
        num2=random.randint(100,500)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2),
                  (f"{num1}//{num2}",num1//num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 7""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 9
    if 80<=points<90:
        if points==80:
            print("lavel 9")
        num1=random.randint(13,50)
        num2=random.randint(3,50)
             #  ("question"  ,  "answer")
        question=[(f"{num1}+{num2}",num1+num2),
                  (f"{num1}-{num2}",num1-num2),
                  (f"{num1}//{num2}",num1//num2),
                  (f"{num1}*{num2}",num1*num2)
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 8""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
            
        #lavel 10
    
    if 90<=points<100:
        if points==90:
            print("lavel 10")
        num1=random.randint(1,10)
        num2=random.randint(2,10)
             #  ("question"  ,  "answer")
        question=[(f"{num1}**2",num1**2),
                  (f"{num2}**3",num2**3)
                  
                 ]
        choice=random.choice(question)          #choice[0]=question  choice[1]=answer
        answer=input(f"""***{choice[0]} Ans  """)
        if answer=="exit":
            print("""you lost
                  lavel 9""")
            break
        ans=int(answer)
        
        if choice[1]==ans:
            print(welcome())
        else:
            print(detect())
        


# In[ ]:





# In[ ]:




