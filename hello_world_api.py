from fastapi import FastAPI

app = FastAPI()

employees = {
    1 : {
        "name" : "Abhijith Sudhakar",
        "designation": "DevOps Engineer",
    }, 
    2 : {
        "name" : "Gayathri S V",
        "designation": "Software Engineer"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-employee/{emp_id}")
async def get_employee(emp_id: int):
    return employees[emp_id]
