from bucket import *

class HashMap:
    def __init__(self):
        self.bucket_count = 4
        self._init_bucket_list()

    def _init_bucket_list(self):
        self.bucket_list = [Bucket() for _ in range(self.bucket_count)]
        self.size = 0

    def _check_size_and_rebuild(self):
        if self.size > (self.bucket_count * 1.2):
            old_bucket_list = self.bucket_list
            self.bucket_count = 2 * self.bucket_count
            self._init_bucket_list()
            for bucket in old_bucket_list:
                while len(bucket) > 0:
                    key, data = bucket.pop_next()
                    self.insert(key, data)

    def insert(self, key, data):
        self._check_size_and_rebuild()
        bucket_index = hash(key) % self.bucket_count
        self.bucket_list[bucket_index].insert(key, data)
        self.size += 1

    def update(self, key, data):
        bucket_index = hash(key) % self.bucket_count
        self.bucket_list[bucket_index].update(key, data)

    def find(self, key):
        bucket_index = hash(key) % self.bucket_count
        return self.bucket_list[bucket_index].find(key)

    def contains(self, key):
        bucket_index = hash(key) % self.bucket_count
        return self.bucket_list[bucket_index].contains(key)

    def remove(self, key):
        bucket_index = hash(key) % self.bucket_count
        self.bucket_list[bucket_index].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)
    
    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for bucket in self.bucket_list:
            ret_str += "Bucket: " + str(bucket) + "\n"
        return ret_str