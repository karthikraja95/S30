class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.bucket_items = 1001  # this is to cover the edge case 1000000
        self.storage = [None] * self.buckets

    def hash_function_1(self, key: int) -> int:
        return key % self.buckets

    def hash_function_2(self, key: int) -> int:
        return key // self.bucket_items

    def add(self, key: int) -> None:
        index = self.hash_function_1(key)
        nested_index = self.hash_function_2(key)
        # if the indx1 of bucket is empty , created nested leaf
        if self.storage[index] is None:
            self.storage[index] = [None] * self.bucket_items
        # should change to True
        self.storage[index][nested_index] = True

    def remove(self, key: int) -> None:
        index = self.hash_function_1(key)
        nested_index = self.hash_function_2(key)
        # if the indx1 of bucket is empty ,return nothing else set that index as False
        if self.storage[index] is None:
            return
        else:
            self.storage[index][nested_index] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.hash_function_1(key)
        nested_index = self.hash_function_2(key)

        if self.storage[index] is None:
            return False
        # return the bool if bucket not none
        return self.storage[index][nested_index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
