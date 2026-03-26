from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
@app.get("/")
def read_root():
    return {"Message": "Hello abhi puli"}

@app.get("/greet")
def greet():
    return {"message":"Hello Sir"}

@app.get("/greet/{name}")
def greet_name(name: str, age : int):
    return {"message": f"Hello {name} and your age is {age}"}

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age":student.age,
        "roll":student.roll 
    }