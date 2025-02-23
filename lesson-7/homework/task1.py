import math

class Vector:
    def __init__(self, *components):
        self.compnents = list(components)
        if not components:
            raise ValueError("Must have at least one component")
    
    def __str__(self):
        return f"Vector{tuple(self.compnents)}"
    
    def __len__(self):
        return (self.compnents)
    
    def _check_dimensions(self, other):
        if len(self) != len(other):
            raise ValueError("Vector dimensions are not valid.")

    def __add__(self, other):
        self._check_dimensions(other)
        result = [a+b for a,b in zip(self.compnents, other.components)]
        return Vector(*result)
    
    def __sub__(self, other):
        self._check_dimensions(other)
        result = [a-b for a,b in zip(self.compnents, other.components)]
        return Vector(*result)
    
    def __mul__(self, other):
        
        if isinstance(other, (int, float)):
            result = [other * c for c in self.components]
            return Vector(*result)
        
        elif isinstance(other, Vector):
            self._check_dimensions(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError(f"Unsupported operand type for *: 'Vector' and '{type(other).__name__}'")

    def __rmul__(self, other):
       
        return self.__mul__(other)

    def magnitude(self):
        
        return math.sqrt(sum(c ** 2 for c in self.components))

    def normalize(self):
        
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        result = [c / mag for c in self.components]
        return Vector(*result)        
        
if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)
    