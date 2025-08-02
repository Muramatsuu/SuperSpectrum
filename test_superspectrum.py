# test_superspectrum.py
"""
Tests for SuperSpectrum module.
"""

import unittest
from superspectrum import SuperSpectrum

class TestSuperSpectrum(unittest.TestCase):
    """Test cases for SuperSpectrum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SuperSpectrum()
        self.assertIsInstance(instance, SuperSpectrum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SuperSpectrum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
