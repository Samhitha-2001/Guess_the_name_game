# -*- coding: utf-8 -*-
import random

def choose():
    name_of_movies=['IRONMAN','ENCANTO','INSIDEOUT','JUMANJI','THOR','AVENGERS','HRIDAYAM','BAHUBALI']
    movie=random.choice(name_of_movies)
    return movie

def correct(y,z):
    m=list(z)
    s=m.count(y)
    if(s==0):
        return False
    else:
        return True
                
def word_with_the_letter(qn,letter,movie):
    y=list(qn)
    x=list(movie)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(x[i]==letter):
            temp.append(x[i])
        else:
            if(y[i]=='*'):
                temp.append('*')
            else:
                temp.append(y[i])
    new_qn=" ".join(str(z) for z in temp)
    return new_qn
    
    
def play():
    willing=True
    while(willing):
        name=input("Enter your name: ")
        score=0
        word=choose()
        x=len(word)
        print("Guess the letters in the name of the movie")
        for i in range(x):
            qn=print("*",end=" ")
        modified_qn=qn
        not_said=True
        while(not_said):
            guess=input("Enter the letter you think is there in the movie: ")
            if(correct(guess,word)):
                print("Yayy...you guessed it right")
                modified_qn=word_with_the_letter(modified_qn,guess,word)
                d=input("If you want to guess the name of the movie then press 1 else if you want to guess another letter then press 2: ")
                if(d==1):
                    ans=input("Enter the movie name: ")
                    if(ans==x):
                        print("Yayy...you are right")
                        score=score+1
                        not_said=False
                    else:
                        print("Oops...you are wrong")
                    c=input("Enter 1 if you wish to continue else enter 0: ")
                    if(c==0):
                        print("Thank you for playing ",name,", your score is ",score)
                        willing=False
                else:
                    continue
            else:
                guess=input("Oops...wrong...guess again: ")
                continue
    
    
        
            
play()       
    
    


