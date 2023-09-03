# can we make rectangle

def can_make_rectangle(a,b,c,d):
    if (a==c and b==d) or(a==b and c==d) or(b==c and a==d)or (a==d and b==c):
        return True
    else:
        return False
cmr=can_make_rectangle(12,2,12,3)
print(cmr)    