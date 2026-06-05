if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    myList=list(set(arr))
    myList.sort()
    runnerUp=myList[-2]
    print(runnerUp)

