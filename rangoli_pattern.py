def print_rangoli(n):
   

    m=n*4-3
    text="abcdefghijklmnopqrstuvwxyz"
    lines=[]

    for i in range(n):
        letters=[]
        for j in range( i+1):
            letters.append(text[n-1-j])
        for j in range(i-1,-1,-1):
            letters.append(text[n-1-j])   
        
        pattern='-'.join(letters).center(m,'-')
        lines.append(pattern)  
    
                
    for line in lines+lines[-2::-1]:
        print(line)        
        
            

        
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)