class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_bucket = 1000
        self.bucktes = [-1] * self.num_bucket

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ind = key % self.num_bucket

        # If the bucket is empty

        if self.bucktes[ind] == -1:
            self.bucktes[ind] = [[key, value]]
            return

        # if the bucket is not empty
        for index, kv in enumerate(self.bucktes[ind]):
            if kv[0] == key:
                self.bucktes[ind][index][1] = value
                return
        self.bucktes[ind].append([key, value])
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or
        -1 if this map contains no mapping for the key
        """
        ind = key % self.num_bucket
        # print("get hashmap",self.buckets[ind])
        if self.buckets[ind] == -1:
            return -1
        for k, v in self.buckets[ind]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        ind = key % self.num_bucket
        ind_to_remove = -1
        if self.buckets[ind] == -1:
            return

        for i, kv_pair in enumerate(self.buckets[ind]):
            if kv_pair[0] == key:
                ind_to_remove = i
                break
        if ind_to_remove == -1:
            return
        else:
            del self.buckets[ind][ind_to_remove]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
