import unittest
from HashMap import HashMap
from MyHashableKey import MyHashableKey


class TestMyHashableKey(unittest.TestCase):

    def setUp(self):
        """Set up a HashMap instance for testing."""
        self.hash_map = HashMap()

    def test_insert_with_myhashablekey(self):
        """Test inserting MyHashableKey into HashMap."""
        key = MyHashableKey(1, "key1")
        self.hash_map.insert(key, "value1")
        self.assertTrue(self.hash_map.contains(key))
        self.assertEqual(self.hash_map.find(key), "value1")

    def test_update_with_myhashablekey(self):
        """Test updating MyHashableKey in HashMap."""
        key = MyHashableKey(2, "key2")
        self.hash_map.insert(key, "value2")
        self.hash_map.update(key, "new_value2")
        self.assertEqual(self.hash_map.find(key), "new_value2")

    def test_remove_with_myhashablekey(self):
        """Test removing MyHashableKey from HashMap."""
        key = MyHashableKey(3, "key3")
        self.hash_map.insert(key, "value3")
        self.hash_map.remove(key)
        self.assertFalse(self.hash_map.contains(key))

    def test_rebuild_with_myhashablekey(self):
        """Test rebuild functionality with MyHashableKey."""
        keys = [MyHashableKey(i, f"key{i}") for i in range(10)]
        for i, key in enumerate(keys):
            self.hash_map.insert(key, f"value{i}")
        old_bucket_count = self.hash_map.bucket_count // 2
        self.assertGreater(self.hash_map.bucket_count, old_bucket_count)
        for i, key in enumerate(keys):
            self.assertEqual(self.hash_map.find(key), f"value{i}")


if __name__ == "__main__":
    unittest.main()
