import unittest
from HashMap import HashMap
from Bucket import Bucket


class TestHashMapBucketConnection(unittest.TestCase):

    def setUp(self):
        """Set up a HashMap instance for testing."""
        self.hash_map = HashMap()

    def test_insert_creates_bucket_entry(self):
        """Test if inserting into HashMap interacts with Bucket."""
        self.hash_map.insert("key1", "value1")
        bucket_index = self.hash_map._get_bucket_index("key1")
        bucket = self.hash_map.bucket_list[bucket_index]
        self.assertTrue(bucket.contains("key1"))

    def test_find_retrieves_from_bucket(self):
        """Test if finding a key in HashMap retrieves from the correct Bucket."""
        self.hash_map.insert("key2", "value2")
        value = self.hash_map.find("key2")
        self.assertEqual(value, "value2")

    def test_update_modifies_bucket_entry(self):
        """Test if updating a key in HashMap modifies the correct Bucket."""
        self.hash_map.insert("key3", "value3")
        self.hash_map.update("key3", "new_value3")
        bucket_index = self.hash_map._get_bucket_index("key3")
        bucket = self.hash_map.bucket_list[bucket_index]
        self.assertEqual(bucket.find("key3"), "new_value3")

    def test_remove_deletes_from_bucket(self):
        """Test if removing a key in HashMap deletes it from the correct Bucket."""
        self.hash_map.insert("key4", "value4")
        self.hash_map.remove("key4")
        bucket_index = self.hash_map._get_bucket_index("key4")
        bucket = self.hash_map.bucket_list[bucket_index]
        self.assertFalse(bucket.contains("key4"))

    def test_rebuild_redistributes_buckets(self):
        """Test if rebuild redistributes keys across new Buckets."""
        for i in range(10):  # Insert enough items to trigger rebuild
            self.hash_map.insert(f"key{i}", f"value{i}")
        old_bucket_count = self.hash_map.bucket_count // 2
        self.assertGreater(self.hash_map.bucket_count, old_bucket_count)
        for i in range(10):
            self.assertEqual(self.hash_map.find(f"key{i}"), f"value{i}")


if __name__ == "__main__":
    unittest.main()
