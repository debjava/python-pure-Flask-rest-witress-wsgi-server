import json

from flask import Blueprint, request

from webapp.entity.Employee import Employee

from webapp.services import EmployeeServices as emp

getAPI = Blueprint('getAPI', __name__)


@getAPI.route("/emp/<empId>")
def getEmpById(empId):
    emp = Employee()
    emp.empId = empId
    emp.firstName = "DD"
    emp.lastName = "Mishra"
    return json.dumps(emp.__dict__)


@getAPI.route("/allEmps")
def getEmployees():
    empList = emp.getEmployees()
    empListAsJson = json.dumps([emp.__dict__ for emp in empList])
    return empListAsJson


# For query parameter
@getAPI.route("/qEmp")
def queryEmp():
    qStr = request.query_string
    print("Query String: ", qStr)
    firstName = request.args.get("fName")
    lastName = request.args.get("lName")
    emp = Employee()
    emp.empId = 13
    emp.firstName = firstName
    emp.lastName = lastName
    return json.dumps(emp.__dict__)
