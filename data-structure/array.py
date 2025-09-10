class MyArrayList:
    
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0
    
    def add_last(self, e):
        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)
        self.data[self.size] = e
        self.size += 1
    
    def add(self, index, e):
        self._check_position_index(index)

        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)
        
        


    def _is_element_index(self, index):
        return 0 <= index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp
    

        