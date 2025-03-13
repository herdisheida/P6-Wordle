from skil.Bucket import Bucket  # LATER - breyta import - eyða "skil."


class HashMap:

    def __init__(self):
        self.item_count = 0  # num of items in the entire data structure
        self.bucket_count = 8  # num of buckets (capacity)

        self.bucket_list = [Bucket() for _ in range(self.bucket_count)]

    def insert(self, key, data):
        """Adds a new key-value pair."""
        self.rebuild()
        index = self._get_bucket_index(key)
        self.bucket_list[index].insert(key, data)
        self.item_count += 1

    def update(self, key, data):
        """Updates existing key-value pair"""
        index = self._get_bucket_index(key)
        self.bucket_list[index].update(key, data)

    def find(self, key):
        """Returns data value for a specific key"""
        return self.bucket_list[self._get_bucket_index(key)].find(key)

    def contains(self, key):
        """Returns True if if key is found in the collection, otherwise False"""
        return self.bucket_list[self._get_bucket_index(key)].contains(key)

    def remove(self, key):
        """Removes the value pair with equal key from the collection"""
        index = self._get_bucket_index(key)
        self.bucket_list[index].remove(key)
        self.item_count -= 1

    def __setitem__(self, key, data):
        """Allows: some_hash_map[key] = data"""
        index = self._get_bucket_index(key)
        if self.contains(key):
            self.bucket_list[index][key] = data
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        """Allows: my_data = some_hash_map[key"""
        return self.find(key)

    def __len__(self):
        """Returns the number of items in the entire data structure"""
        return self.item_count

    def rebuild(self):
        """When the num of items in the HashMap reach 120% of the num of buckets,
        Double the arrays capacity and redistributes all key-value pairs"""
        if self.item_count >= self.bucket_count * 1.2:
            old_bucket_list = self.bucket_list

            self.bucket_count *= 2
            self.bucket_list = [Bucket() for _ in range(self.bucket_count)]
            self.item_count = 0  # reset before redistributing

            for bucket in old_bucket_list:
                node = bucket.head
                while node:
                    self.insert(node.key, node.data)
                    node = node.next

    def _get_bucket_index(self, key):
        """Get index"""
        return hash(key) % self.bucket_count

    def __str__(self):
        """testing HASH MAP str"""
        # DELETE - þessi klasi hefur ekki __str__ func
        ret = ""
        for x in self.bucket_list:
            ret += str(x)
        return ret
