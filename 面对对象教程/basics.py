"""
简单的面向对象入门示例
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"大家好，我是{self.name}，今年 {self.age} 岁。"


if __name__ == "__main__":
    p = Person("小明", 20)
    print(p.greet())
