def permutation(set):
    empty_lst=[]
    for i in range(len(set)):
        m=set[i]
        rest_lst=set[:i]+set[i+1:]
        for j in permutation(rest_lst):
            empty_lst.append([m]+j)
    return empty_lst

def check_perm(set):
    try:
        permutation(set)
    except ValueError:
        print("empty list or one element")
        

def main():
    set=str(input("What is the string"))
    print(check_perm(set))
    print(permutation(set))
    
main()