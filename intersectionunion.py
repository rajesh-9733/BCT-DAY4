s={2,4,5,1,0}
t={2,4,5,7,9,6}
s.pop()
t.pop()
print(s)
print(t)
k=s.intersection(t)
print("intersection of set is:",k)
u=s.union(t)
print("union of set is:",u)
print("if s is subset of t",s.issubset(s))
print("if s is superset of t",s.issuperset(t))
