from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_onet(self):
        self.assertEqual(solution([1,2,3,4]),[1,3,6,10])
    def test_example_two(self):
        self.assertEqual(solution([1,1,1,1,1]),[1,2,3,4,5])
    def test_example_three(self):
        self.assertEqual(solution([3,1,2,10,1]),[3,4,6,16,17])