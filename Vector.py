class Vector:
    """ Represent a vector in multidimensional space """
    def __init__(self, d):
        self._coords = [0]*d

    def __len__(self):
        ''' Return the dimension of the vector '''
        return len(self._coords)

    def __getitem__(self, j):
        ''' Return the jth coordinate of the vector '''
        return self._coords[j]

    def __setitem__(self, j, val):
        ''' Set the jth value of the vector to the given val'''
        self._coords[j] = val

    def __add__(self, other):
        ''' Return sum of two vectors '''
        if len(self) != len(other):             # relies on len method
            raise ValueError("The vectors must be of equal dimension")

        result = Vector(len(self))              # start with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        ''' Return true if the vector has the same coordinates as the other '''
        return self._coords == other._coords
    def __ne__(self, other):
        ''' Return True if the vectors are not equal '''
        return not self == other                # relies on existing __eq__ function

    def __str__(self):
        ''' Produce string representation of vector '''
        return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation


u = Vector(4)
u[1] = 3
v = Vector(4)
v[1] = 5
k = v + u
print(k)