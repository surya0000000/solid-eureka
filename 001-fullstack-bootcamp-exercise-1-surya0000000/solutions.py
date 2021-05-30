def biggest():

 # Problem 1
 l=[1,2,3,4]
 max=0
 for i in l:
        if max<i:
                  max=i
 print(max)  
 
def average(l):
    # Problem 2
    avg=0
    n=0
    for i in l:
        avg+=i
        n+=1;
    avg/=n;
    return(avg)

  
def longest(s):
    # Problem 3
    a=0
    b=""
    for i in s:
        if len(i)>a:
           a=len(i)
           b=i
        
    return(b)    

    

def first_space(l):
    # Problem 4
    
    for i in l:
        for j in i:
            if j==" ":
                return i
                
def freq(corpus_word):
  letter_freq = dict()
  
  for letter in range(len(corpus_word)):
    if corpus_word[letter] not in letter_freq:
        letter_freq[corpus_word[letter]] = 1

    else:
         letter_freq[corpus_word[letter]] += 1
 
  return letter_freq                
    

 
def panagram(s):
    # Problem 6
    
    arr=[0]*26
    for i in s:
      if i!=" ":
        arr[ord(i)-97]+=1
    
    for i in arr:
         if i<1:
           return false
           
    return true       
    
                

def abbreviate(s):
    # Problem 7
    sa=""
    for ind,val in enumerate(s):
       if val.isupper():
         sa=sa+s[ind]
    
    return(sa)
    
def split(amount, denominations):
    # Problem 8
    
    d=dict()
    for i in denominations:
      if i!=0 and int(amount/i)!=0:
        d[i]=int(amount/i)
        amount%=i*d[i]
    
    return(d)
        

