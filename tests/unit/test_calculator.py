"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract , multiply , power, sqrt   

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, 3) == -8
        assert subtract(-10, -4) == -6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

class TestMultiplyDivide:
    """Test multiplication and division operations."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20

    def test_multiply_negative_numbers(self):
        """Test multiplying with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-5, -4) == 20

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(6, 3) == 2
        assert divide(20, 4) == 5

    def test_divide_negative_numbers(self):
        """Test dividing with negative numbers."""
        assert divide(-6, 3) == -2
        assert divide(-20, -4) == 5

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


    class TestPower:
        """Test exponentiation (power) operation."""

        def test_power_positive_numbers(self):
            """Test raising positive numbers to positive powers."""
            assert power(2, 3) == 8
            assert power(5, 2) == 25

        def test_power_zero_exponent(self):
            """Test any number to the power of zero is 1."""
            assert power(10, 0) == 1
            assert power(-3, 0) == 1

        def test_power_negative_exponent(self):
            """Test raising numbers to negative exponents."""
            assert power(2, -2) == 0.25
            assert power(-2, -3) == -0.125

        def test_power_input_validation(self):
            """Test power rejects non-numeric inputs."""
            with pytest.raises(TypeError, match="Power function requires numeric inputs"):
                power("2", 3)
            with pytest.raises(TypeError, match="Power function requires numeric inputs"):
                power(2, "3")


    class TestSqrt:
        """Test square root operation."""

        def test_sqrt_positive_numbers(self):
            """Test square root of positive numbers."""
            assert sqrt(4) == 2
            assert sqrt(9) == 3
            assert sqrt(0) == 0

        def test_sqrt_float(self):
            """Test square root of float numbers."""
            assert sqrt(2.25) == 1.5

        def test_sqrt_negative_number(self):
            """Test square root of negative number raises ValueError."""
            with pytest.raises(ValueError, match="Cannot take square root of negative number"):
                sqrt(-4)

        def test_sqrt_input_validation(self):
            """Test sqrt rejects non-numeric input."""
            with pytest.raises(TypeError, match="Square root requires a numeric input"):
                sqrt("16")
 