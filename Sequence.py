from abc import abstractmethod, ABCMeta

class Sequence(metaclass = ABCMeta):

    @abstractmethod
    def __len__(self):

    @abstractmethod
    def __getitem__(self, j):