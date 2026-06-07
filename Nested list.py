if __name__ == '__main__':
    records=[]
    scores=[]
    second_lowestName=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    scores=list(set(scores))
    scores.sort()
    second_lowest=scores[1]
    for student in records:
        if student[1]==second_lowest:
            second_lowestName.append(student[0])
            
    second_lowestName.sort()  
    for name in  second_lowestName:
      print( name)      