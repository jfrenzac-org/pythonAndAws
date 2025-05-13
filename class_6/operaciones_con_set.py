set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union {1,2,3,4,5,6}

print("Unión", set_a.union(set_b))
print("Unión", set_a | set_b)

# Intersección {3,4}

print("Intersección", set_a.intersection(set_b))
print("Intersección", set_a & set_b)

# Diferencia (A - B) {1,2}
print("Diferencia (A -B): ", set_a.difference(set_b))
