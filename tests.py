import unittest
import time
from main import summarize, multiplication, maximal, minimal, is_valid


class TestMath(unittest.TestCase):
    def test_summarize(self):
        self.assertEquals(summarize([3, 7]), 10)
        self.assertEquals(summarize([3.7, 0.3]), 4)
        self.assertEquals(summarize([-6, 8]), 2)
        self.assertEquals(summarize([-0.6, 5]), 4.4)
        self.assertEquals(summarize([-0.6, 5]), 4.4)

    def test_multiplication(self):
        self.assertEquals(multiplication([5, 4]), 20)
        self.assertEquals(multiplication([-0.4, 7, 2]), -5.6)
        self.assertEquals(multiplication([0, 100]), 0)
        self.assertEquals(multiplication([8, 7, 1]), 56)
        self.assertEquals(multiplication([-9, -1, -3]), -27)

    def test_maximal(self):
        self.assertEquals(maximal([3, 6, 5]), 6)
        self.assertEquals(maximal([0, 2]), 2)
        self.assertEquals(maximal([0.4, -3, 8.9]), 8.9)
        self.assertEquals(maximal([0, 0]), 0)
        self.assertEquals(maximal([0, 0.1]), 0.1)

    def test_minimal(self):
        self.assertEquals(minimal([5, 8, 1]), 1)
        self.assertEquals(minimal([-25, 25, 1]), -25)
        self.assertEquals(minimal([i for i in range(1000)]), 0)
        self.assertEquals(minimal([-25, 25, 1]), -25)
        self.assertEquals(minimal([0.23, -0.01]), -0.01)

    def tast_is_valid(self):
        self.assertEquals(is_valid(['7', '3']), True)
        self.assertEquals(is_valid([' 10 ']), False)
        self.assertEquals(is_valid(['jsidyfdcjn', 'wedzsxfd']), False)
        self.assertEquals(is_valid(['6,5']), False)
        self.assertEquals(is_valid(['1.9', '2.1', '22.2']), True)


def test_time_summarize():
    start_time = time.time()
    a = summarize(i for i in range(10000000))
    print(time.time() - start_time)


def test_time_multiplication():
    start_time = time.time()
    a = multiplication(i for i in range(10000000))
    print(time.time() - start_time)


def test_time_maximal():
    start_time = time.time()
    a = maximal(i for i in range(10000000))
    print(time.time() - start_time)


def test_time_minimal():
    start_time = time.time()
    a = minimal(i for i in range(10000000))
    print(time.time() - start_time)


def test_time_is_valid():
    start_time = time.time()
    a = is_valid(i for i in range(10000000))
    print(time.time() - start_time)


test_time_summarize()
test_time_multiplication()
test_time_maximal()
test_time_minimal()
test_time_is_valid()
unittest.main()
