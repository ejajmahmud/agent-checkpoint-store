"""Unit tests for CheckpointStore."""
import unittest
from agent_checkpoint_store.store import CheckpointStore

class TestCheckpointStore(unittest.TestCase):
    def test_checkpoint_and_rollback(self):
        store = CheckpointStore()
        store.set_state("counter", 10)
        store.set_state("items", ["a", "b"])
        store.create_checkpoint("start")

        store.set_state("counter", 99)
        store.set_state("items", ["a", "b", "c"])
        self.assertEqual(store.get_state("counter"), 99)

        ok = store.rollback("start")
        self.assertTrue(ok)
        self.assertEqual(store.get_state("counter"), 10)
        self.assertEqual(store.get_state("items"), ["a", "b"])

if __name__ == "__main__":
    unittest.main()
