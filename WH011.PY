from ast import If


name = str(input())


math = int(input())
science = int(input())
art = int(input())
PE = int(input())
literature = int(input())


if math > 12  :
    print("math: failed")
else:
    print(f'math: paased')    
if  science > 12  :
    print("science: failed")     
else:
    print(f'science: paaesd') 
if  art > 12  : 
    print("art: failed")      
else:
    print(f'art: paased')
if  PE > 12  :
    print("PE: failed")  
else:
    print(f'PE: paased')   
if  literature < 12  :
    print("literature: failed")
else:
    print(f'literature: paased')
print(f'scores: [{math}, {science}, {art} ,{PE}, {literature}]')    

        


