square=[x**2 for x in range(1,5)]
cube=[(x,k) for j in square for k in range(1,5) if True]
print square
print cube
dicsquare={a:a**2 for a in range(1,5)}
print dicsquare
setsquare={x for x in range(1,6)}
print setsquare
