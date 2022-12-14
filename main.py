from enum import Enum
from fastapi import FastAPI

class EmployeeName(str, Enum):
    
    abhijith = "abhijith"
    gayathri = "gayathri"
    naveen = "naveen"
    vinaya = "vinaya"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# google.com/get-employee/
@app.get("/get-employee-name/{emp_name}")
async def get_employee_name(emp_name: EmployeeName):
    
    if emp_name is emp_name.abhijith:
        return {"emp_name": emp_name, "message": "Employee name is Abhiijth!"}
    
    if emp_name.value == "gayathri":
        return {"emp_name": emp_name, "message": "Employee name is Gayathri"}

    return {"emp_name": emp_name, "message": "Employee name is Naveen or Vinaya!"}
