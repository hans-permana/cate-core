"""
Test the IO operations
"""

import os
import unittest
from unittest import TestCase

from cate.ops.io import open_dataset, save_dataset


class TestIO(TestCase):
    @unittest.skip(reason="skipped unless you want to debug data source access")
    def test_open_dataset(self):
        # Test normal functionality
        dataset = open_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-01-01', '2008-03-01')
        self.assertIsNotNone(dataset)

        # Test swapped dates
        with self.assertRaises(ValueError):
            open_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-03-01', '2008-01-01')

        # Test required arguments
        with self.assertRaises(TypeError):
            open_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-03-01')

    @unittest.skip(reason="skipped unless you want to debug data source access")
    def test_save_dataset(self):
        # Test normal functionality
        dataset = open_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-01-01', '2008-03-01')
        save_dataset(dataset, 'remove_me.nc')
        self.assertTrue(os.path.isfile('remove_me.nc'))
        os.remove('remove_me.nc')

        # Test required arguments
        with self.assertRaises(TypeError):
            save_dataset(dataset)

        # Test behavior when passing unexpected type
        with self.assertRaises(NotImplementedError):
            dataset = ('a', 1, 3, 5)
            save_dataset(dataset, 'remove_me.nc')

        self.assertFalse(os.path.isfile('remove_me.nc'))
