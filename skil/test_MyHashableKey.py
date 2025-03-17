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

    def test_myhashablekey_equality(self):
        """Test equality of MyHashableKey instances."""
        key1 = MyHashableKey(1, "key")
        key2 = MyHashableKey(1, "key")
        key3 = MyHashableKey(2, "key")
        key4 = MyHashableKey(1, "different_key")
        self.assertTrue(key1 == key2)
        self.assertFalse(key1 == key3)
        self.assertFalse(key1 == key4)

    def test_myhashablekey_hash(self):
        """Test hash consistency and uniqueness for MyHashableKey."""
        key1 = MyHashableKey(1, "key")
        key2 = MyHashableKey(1, "key")
        key3 = MyHashableKey(2, "key")
        key4 = MyHashableKey(1, "different_key")
        self.assertEqual(hash(key1), hash(key2))  # Equal keys must have the same hash
        self.assertNotEqual(hash(key1), hash(key3))  # Different keys should have different hashes
        self.assertNotEqual(hash(key1), hash(key4))  # Different keys should have different hashes

    def test_myhashablekey_empty_string(self):
        """Test MyHashableKey with an empty string."""
        key1 = MyHashableKey(1, "")
        key2 = MyHashableKey(1, "")
        self.assertTrue(key1 == key2)
        self.assertEqual(hash(key1), hash(key2))

    def test_myhashablekey_negative_integer(self):
        """Test MyHashableKey with a negative integer."""
        key1 = MyHashableKey(-1, "key")
        key2 = MyHashableKey(-1, "key")
        self.assertTrue(key1 == key2)
        self.assertEqual(hash(key1), hash(key2))

    def test_myhashablekey_special_characters(self):
        """Test MyHashableKey with special characters in the string."""
        key1 = MyHashableKey(1, "!@#$%^&*()")
        key2 = MyHashableKey(1, "!@#$%^&*()")
        self.assertTrue(key1 == key2)
        self.assertEqual(hash(key1), hash(key2))

    def test_myhashablekey_large_integer(self):
        """Test MyHashableKey with a very large integer."""
        key1 = MyHashableKey(2**31, "key")
        key2 = MyHashableKey(2**31, "key")
        self.assertTrue(key1 == key2)
        self.assertEqual(hash(key1), hash(key2))

    def test_myhashablekey_unicode_characters(self):
        """Test MyHashableKey with Unicode characters in the string."""
        key1 = MyHashableKey(1, "ключ")  # "ключ" means "key" in Russian
        key2 = MyHashableKey(1, "ключ")
        self.assertTrue(key1 == key2)
        self.assertEqual(hash(key1), hash(key2))

    def test_myhashablekey_self_comparison(self):
        """Test MyHashableKey is equal to itself."""
        key = MyHashableKey(1, "key")
        self.assertTrue(key == key)


if __name__ == "__main__":
    unittest.main()
