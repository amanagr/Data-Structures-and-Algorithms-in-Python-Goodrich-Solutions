class SequenceIterator:
    ''' An Iterator for any of python's sequence types'''
    def __init__(self, sequence):
        ''' Create an iterator for a given sequence '''
        self._seq = sequence        # keep a reference to the underlying data
        self._k = -1                # will increment to 0 on first call to __next__

    def __next__(self):
        """ Return the next element, or else raise a StopIteration error. """
        self._k += 1                # advance to next index
        if(self._k) < len(self._seq):   
            return self._seq[self._k]   # return the data element
        else :
            raise StopIteration() # there are no more elements 

    def __iter__(self):
        ''' By Convention the iterator must return itself as an iterator'''
        return self


        