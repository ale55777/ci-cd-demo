"""
Unit tests for the app module.
"""

import pytest
from app import add_numbers


class TestAddNumbers:
    """Test suite for the add_numbers function."""
    
    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add_numbers(5, 3) == 8
        assert add_numbers(10, 20) == 30
    
    def test_add_negative_integers(self):
        """Test adding negative integers."""
        assert add_numbers(-5, -3) == -8
        assert add_numbers(-10, 5) == -5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add_numbers(3.5, 2.5) == 6.0
        assert add_numbers(1.1, 2.2) == pytest.approx(3.3)
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add_numbers(0, 0) == 0
        assert add_numbers(5, 0) == 5
        assert add_numbers(0, 10) == 10
    
    def test_add_mixed_types(self):
        """Test adding integers and floats."""
        assert add_numbers(5, 2.5) == 7.5
        assert add_numbers(3.3, 2) == pytest.approx(5.3)
    
    def test_invalid_input_string(self):
        """Test that string inputs raise TypeError."""
        with pytest.raises(TypeError):
            add_numbers("5", 3)
        
        with pytest.raises(TypeError):
            add_numbers(5, "3")
    
    def test_invalid_input_none(self):
        """Test that None inputs raise TypeError."""
        with pytest.raises(TypeError):
            add_numbers(None, 5)
        
        with pytest.raises(TypeError):
            add_numbers(5, None)
    
    def test_invalid_input_list(self):
        """Test that list inputs raise TypeError."""
        with pytest.raises(TypeError):
            add_numbers([1, 2], 3)
