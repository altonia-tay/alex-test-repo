"""示例应用模块 - 用于测试 CI/CD 流水线"""

from typing import Optional


def add(a: int, b: int) -> int:
    """两个数相加"""
    return a + b


def subtract(a: int, b: int) -> int:
    """两个数相减"""
    return a - b


def multiply(a: int, b: int) -> int:
    """两个数相乘"""
    return a * b


def divide(a: int, b: int) -> float:
    """两个数相除"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def greet(name: Optional[str] = None) -> str:
    """生成问候语"""
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Alex"))
    print(f"1 + 2 = {add(1, 2)}")
