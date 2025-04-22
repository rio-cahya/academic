from itertools import permutations

def pertandingan(A,B,skill,order):
    skill = skill_0
    for i in order:
        if skill >= A[i]:
            skill +=B[i]
        else:
            return False
    return True
    
def find_order(A,B,skill_0,N):
    indeks = list(range(N))
    for order in permutations(indeks):
        if pertandingan(A,B,skill_0,order):
            return urutan
    return None
    


N=4
A=[8,9,3,2]
B=[5,4,1,3]
skill_0=2
win = find_order(A,B,skill_0,N)

if win:
    print("Kemenangan",win)
else:
    print("Tidak bisa menang")
