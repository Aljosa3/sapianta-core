import unittest

from runtime.replay.replay_engine import replay_all


class TestReplayDeterminism(unittest.TestCase):

    def test_replay_integrity(self):

        results = replay_all()

        for r in results:
            assert r["match"], f"Divergence detected: {r}"


if __name__ == "__main__":
    unittest.main()