from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = "User" # setting default value
    age: Optional[int] = None # default
    email: str
    cgpa: float = Field(gt=0, lt=10, default=6.9, description="A decimal value representing the cgpa of the student") # greater than 0 less than 10

new_student = {
    "name": "Keshav",
    "age": "32",
    "email": "abc@gmail.com",
    "cgpa": 5.9
}

student = Student(**new_student)

print(dict(student))