from enum import Enum
from fastapi import FastAPI


class EmployeeName(str, Enum):
    
    emp_name_1 = "abhijith"
    emp_name_2 ="gayathri"
    emp_name_3 = "naveen"
    emp_name_4 = "vinaya"


app = FastAPI()

# without parameter type the value your function received will be str
# google.com/get-employee/1

# @app.get("/get-employee/{emp_id}")
# async def get_employee(emp_id):
#     return {"emp_id": emp_id}

# with parameter type automatic parsing and data validation happens
# google.com/get-employee/1

@app.get("/get-employee/{emp_id}")
async def get_employee(emp_id: int):
    return {"emp_id": emp_id}
    
# predefined values
# google.com/get-employee-name/abhijith

@app.get("/get-employee-name/{emp_name}")
async def get_employee_name(emp_name: EmployeeName):
    
    # compare with enumeration member
    if emp_name is emp_name.emp_name_1:
        return {"emp_name": emp_name, "message": "Employee name is Abhiijth!"}
    
    # get enumeration value
    if emp_name.value == "gayathri":
        return {"emp_name": emp_name, "message": "Employee name is Gayathri"}

    return {"emp_name": emp_name, "message": "Employee name is Naveen or Vinaya!"}


# containing paths
# google.com/get-files/{file_path}
# {file_path} itself to contain a path, like resumes/abhijith.pdf
# the URL for that file would be something like: get-files/resumes/abhijith.pdf

@app.get("/get-files/{file_path:path}")
async def get_file(file_path: str):
    return {"file_path": file_path}
