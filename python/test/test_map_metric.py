import unittest
import sys
''' Testing file
    Run with `python -m unittest in the root folder'''


class TimeRangeTestCase(unittest.TestCase):
    '''Tests for timerange creation'''
    
    def test_outoforder_times(self):
        '''Test if the proper error is thrown with time1=9 and time2=8'''
        with self.assertRaises(ValueError) as cm:
            _get_timerange(9,8)
        self.assertEqual('start time 09:00:00 after end time 08:00:00', str(cm.exception))
        
    def test_valid_range(self):
        '''Test if the right string is produced from time1=8 and time2=9'''
        valid_result = 'timerange(\'08:00:00\'::time, \'09:00:00\'::time)'
        self.assertEqual(valid_result, _get_timerange(8,9))
        
    def test_equal_numbers(self):
        '''Test if the proper error is thrown if both parameters are equal'''
        with self.assertRaises(ValueError) as cm:
            _get_timerange(8,8)
        self.assertEqual('2nd time parameter 8 must be at least 1 hour after first parameter 8', str(cm.exception))



if __name__ == '__main__':
    unittest.main()