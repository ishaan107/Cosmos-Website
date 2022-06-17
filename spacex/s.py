
def find_permutation(s):
        s,l,n=s*2,[],len(s)
        s1=s[::-1]
        for i in range(n):
            l.append(s[i:i+n])
            l.append(s1[i:i+n])
        return sorted(list(set(l)))




w=find_permutation('abcd')
print(w)