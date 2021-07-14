from vector.Vector import Vector, VectorComponent

vector = Vector()
vector.add(VectorComponent(index=100, number=1))
vector.add(VectorComponent(index=200, number=2))
vector.add(VectorComponent(index=300, number=3))
vector.add(VectorComponent(index=400, number=4))
vector.add(VectorComponent(index=500, number=5))
vector.add(VectorComponent(index=600, number=6))
vector.add(VectorComponent(index=700, number=7))
vector.add(VectorComponent(index=800, number=8))

print(vector.vector())
print(vector.restriction(vectorPart=(300, 400, 500, 600)))