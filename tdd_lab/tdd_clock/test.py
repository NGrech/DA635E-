import unittest
from parameterized import parameterized

from tdd_clock.clock.clock import Clock

class TestClock(unittest.TestCase):
    
    # Clock initialization tests 

    def test_init_default_state_value(self):
        clock = Clock()
        self.assertEqual(clock._state, 1)

    def test_init_default_time_values(self):
        clock = Clock()
        self.assertEqual(clock._the_time._the_hour, 0)
        self.assertEqual(clock._the_time._the_minute, 0)
        self.assertEqual(clock._the_time._the_second, 0)

    def test_init_default_date_values(self):
        clock = Clock()
        self.assertEqual(clock._the_date._the_day, 1)
        self.assertEqual(clock._the_date._the_month, 1)
        self.assertEqual(clock._the_date._the_year, 2000)

    # State transition tests

    def test_s1_change_mode(self):
        clock = Clock()
        output = clock.change_mode()
        self.assertEqual(output, '00:00:00 1/1/2000')
        self.assertEqual(clock._state, 2)

    def test_s1_ready(self):
        clock = Clock()
        output = clock.ready()
        self.assertEqual(output, '00:00:00')
        self.assertEqual(clock._state, 3)

    def test_s1_set(self):
        clock = Clock()
        self.assertRaises(ValueError, clock.set(1,1,1))

    # TODO: Test transitions from S2

    def test_s3_change_mode(self):
        clock = Clock()
        clock._state = 3
        self.assertRaises(ValueError, clock.change_mode())

    def test_s3_ready(self):
        clock = Clock()
        clock._state = 3
        self.assertRaises(ValueError, clock.ready())

    def test_s3_ready(self):
        clock = Clock()
        clock._state = 3
        output = clock.set(1,1,1)
        self.assertEqual(output, '01:01:01')
        self.assertEqual(clock._state, 2)

    # TODO: Test transitions from S4

    # Time boundary testing 

    @parameterized.expand([(0,), (1,), (22,), (23,)])
    def test_valid_hour_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        output = clock.set(bound, 2, 2)
        self.assertEqual(output, f'{bound:02}:02:02')
        self.assertEqual(clock._state, 1)

    @parameterized.expand([(-1,), (24,)])
    def test_invalid_hour_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        self.assertRaises(ValueError, clock.set(bound, 2, 2))

    @parameterized.expand([(0,), (1,), (58,), (59,)])
    def test_valid_min_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        output = clock.set(2, bound, 2)
        self.assertEqual(output, f'02:{bound:02}:02')
        self.assertEqual(clock._state, 1)

    @parameterized.expand([(-1,), (60,)])
    def test_invalid_min_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        self.assertRaises(ValueError, clock.set(2, bound, 2))

    @parameterized.expand([(0,), (1,), (58,), (59,)])
    def test_valid_sec_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        output = clock.set(2, 2, bound)
        self.assertEqual(output, f'02:02:{bound:02}')
        self.assertEqual(clock._state, 1)

    @parameterized.expand([(-1,), (60,)])
    def test_invalid_min_boundaries(self, bound):
        clock = Clock()
        clock._state = 3
        self.assertRaises(ValueError, clock.set(2, 2, bound))

    # TODO: test boundaries for Date object

if __name__ == '__main__':
    unittest.main()
