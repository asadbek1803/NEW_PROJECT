# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:27:19 2022

@author: User 4
"""
savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 4000
    elif 7<=yosh<18:
        narh = 9000
    elif 18<=yosh<65:
        narh = 15000
    else: narh = 0
    
    
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
