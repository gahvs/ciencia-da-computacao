from vector.Vector import Vector, VectorComponent

vector = Vector()
vector.add(VectorComponent(index=100, number=1))
vector.add(VectorComponent(index=200, number=2))
vector.add(VectorComponent(index=300, number=3))
vector.add(VectorComponent(index=400, number=4))

vector2 = Vector()
vector2.add(VectorComponent(index=100, number=5))
vector2.add(VectorComponent(index=200, number=6))
vector2.add(VectorComponent(index=300, number=7))
vector2.add(VectorComponent(index=400, number=8))

Vector.copy