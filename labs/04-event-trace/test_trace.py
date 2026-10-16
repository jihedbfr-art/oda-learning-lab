import copy
import unittest
from event_trace import load_events, replay


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.events = load_events()

    def test_duplicate_changes_naive_total_only(self):
        self.assertEqual(replay(self.events, idempotent=False)["credits"], 6)
        self.assertEqual(replay(self.events)["credits"], 3)

    def test_disorder_is_buffered_and_drained(self):
        result = replay(self.events)
        self.assertEqual(result["applied"], ["open-A", "restore-A", "credit-A", "review-A"])
        self.assertEqual(result["pending"], [])
        self.assertEqual(result["out_of_order"], ["restore-A"])

    def test_late_event_is_visible(self):
        self.assertEqual(replay(self.events)["late"], ["review-A"])

    def test_replaying_twice_has_one_effect(self):
        self.assertEqual(replay(self.events + self.events)["credits"], 3)

    def test_gap_stays_pending(self):
        events = [e for e in self.events if e["id"] != "restore-A"]
        result = replay(events)
        self.assertEqual(result["credits"], 0)
        self.assertEqual(result["pending"], [3, 4])

    def test_conflicting_duplicate_is_rejected(self):
        event = copy.deepcopy(self.events[1])
        event["credits"] = 9
        with self.assertRaises(ValueError):
            replay(self.events + [event])

    def test_invalid_event_is_rejected(self):
        for field, value in (("sequence", True), ("occurred", -1), ("credits", "3"),
                             ("kind", "unknown"), ("received", -1)):
            events = copy.deepcopy(self.events)
            events[1][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                replay(events)

    def test_missing_field_is_rejected(self):
        events = copy.deepcopy(self.events)
        del events[0]["incident"]
        with self.assertRaises(ValueError):
            replay(events)

    def test_duplicate_sequence_is_rejected(self):
        events = copy.deepcopy(self.events)
        events[2]["sequence"] = 3
        with self.assertRaises(ValueError):
            replay(events)

    def test_no_mutation(self):
        before = copy.deepcopy(self.events)
        replay(self.events)
        self.assertEqual(self.events, before)


if __name__ == "__main__":
    unittest.main()
