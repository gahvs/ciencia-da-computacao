from vector.Vector import Vector, VectorComponent

vector = Vector()
vector.add(VectorComponent(index=100, number=0))
vector.add(VectorComponent(index=200, number=0))
vector.add(VectorComponent(index=300, number=0))
vector.add(VectorComponent(index=400, number=0))
vector.add(VectorComponent(index=500, number=0))
vector.add(VectorComponent(index=600, number=0))
vector.add(VectorComponent(index=700, number=0))
vector.add(VectorComponent(index=800, number=0))

print(vector.vector())
print(vector.isNull())