from algebra.vector import VectorComponent, Vector

vector = Vector()
vector2 = Vector()

vector.add(VectorComponent(1, 2))
vector.add(VectorComponent(2, 3))
vector.add(VectorComponent(3, 4))

vector2.add(VectorComponent(1, 2))
vector2.add(VectorComponent(2, 3))
vector2.add(VectorComponent(3, 4))

print(vector.vector())
print(vector2.vector())

print(Vector.product(vector, vector2))