
#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    s = string
    l=list(s)
    l[position]=character
    s=''.join(l) 
    
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)