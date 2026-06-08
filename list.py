if __name__ == '__main__':
    N = int(input())
    my_list=[]
    
    for i in range(N):
        n=input().split()
        if n[0]=='append':
               my_list.append(int(n[1]))
        elif n[0]=='remove':
            
            my_list.remove(int(n[1]))    
                 
        elif n[0]=='insert':
            my_list.insert(int(n[1]),int(n[2]))
            
        elif n[0]=='reverse':
             my_list.reverse()
             
        elif n[0]=='sort':
             my_list.sort()
        elif n[0]=='pop':
             my_list.pop()
                 
        elif n[0]=='print' :   
            print(my_list)
    
    