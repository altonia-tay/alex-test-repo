"""应用测试模块"""

import pytest
from app import add, subtract, multiply, divide, greet


class TestMathOperations:
    """数学运算测试"""
    
    def test_add(self):
        """测试加法"""
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtract(self):
        """测试减法"""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
    
    def test_multiply(self):
        """测试乘法"""
        assert multiply(3, 4) == 12
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        """测试除法"""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """测试除零异常"""
        with pytest.raises(ValueError):
            divide(10, 0)


class TestGreet:
    """问候函数测试"""
    
    def test_greet_default(self):
        """测试默认问候"""
        assert greet() == "Hello, World!"
    
    def test_greet_with_name(self):
        """测试带名字的问候"""
        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"
