from vpython import box, color, vector
from math import *

A = vector(1,2,-1)

data = ["one", "two", "three"]
for idx, val in enumerate(data): print(f'{idx}:{val}')

box(color=color.red)

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

"""
class Person {
public:
    Person(std::string name, int alter) {
        this->name = name;
        this->alter = alter;
    }

private:
    std::string name;
    int alter;
};
"""
