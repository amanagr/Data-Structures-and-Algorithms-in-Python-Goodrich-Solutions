class Range:
    ''' A class that mimics the built in range class'''
    def __init__(self,start, stop = None, step = 1):
        """ Initialize a range instance
        Semantics is similar to built in range class.
        """
        if (step == 0):
            raise ValueError("Step cannot be zero")
        
        if stop is None:        # Special case of range(n)
            start, stop = 0, start  # should be treated a if range(0, n)

        # calculate the effective length once
        self._len = max(0, (stop - start + step -1)//step)

        # need knowledge of start and step (but not stop) to support getitem

        self._start = start
        self._step = step


    def __len__(self):
        """Return number of entries in the range."""

        return self._length

    def __getitem__(self, k):

        """Return entry at index k (using standard interpretation if negative). """

        if k < 0:

            k += len(self)
            # attempt to convert negative index
        if not 0 <= k < self._len:
            raise IndexError( 'index out of range ')
        return self._start + k * self._step

print([x for x in Range(-1,10,5)])