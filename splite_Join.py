

def split_and_join(line):
    
    lineList=line.split(" ")
    lineJoin="-".join(lineList)
    
    return lineJoin

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)