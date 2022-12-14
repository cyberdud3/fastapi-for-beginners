from fastapi import FastAPI, Path
from typing import List, Optional, Union


app = FastAPI()

employees = {
    1 : {
        "name" : "Abhijith",
        "designation" : "DevOps Engineer",
    }, 
    2 : {
        "name" : "Gayathri",
        "designation" : "Software Engineer"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

# google.com/get-employee/1
@app.get("/get-employee/{emp_id}")
async def get_employee(emp_id: int = Path(None,
    description="The ID of an employee you want to view.",
    gt=0,
    lt=3)):

    return employees[emp_id]

# google.com/get-by-name?search=Abhijith
@app.get("/get-employee-by-name")
async def get_employee_by_name(*, emp_name: Optional[str] = None, test: int):

    for emp_id in employees:
        if employees[emp_id]["name"] == emp_name:
            return employees[emp_id]

    return {"Data": "Not Found"}
