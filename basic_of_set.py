s={1,2,3,5,9}
s.add(7)
print(s)
s.discard(3)
print(s)
s1={6,4,8}
s.update(s1)
print(s)



b={3,5,7}
print(s.union(b))
print(s.intersection(b))
print(s.issuperset(b))
print(s.isdisjoint(b))
print(s.difference(b))
print(s.issubset(b))