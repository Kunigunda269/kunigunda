import runner
import unittest


def test_walk(self):
    runner = Runner("TestRunner1")
    for _ in range(10):
        runner.walk()
    self.assertEqual(runner.distance, 50, "Distance should be 50 after 10 walks.")


def test_run(self):
    runner = Runner("TestRunner2")
    for _ in range(10):
        runner.run()
    self.assertEqual(runner.distance, 100, "Distance should be 100 after 10 runs.")


def test_challenge(self):
    runner1 = Runner("Runner1")
    runner2 = Runner("Runner2")
    for _ in range(10):
        runner1.run()
        runner2.walk()
    self.assertNotEqual(runner1.distance, runner2.distance, "Distances should not be equal for different activities.")
