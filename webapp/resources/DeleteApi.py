from flask import Blueprint, Response

from webapp.entity.Employee import Employee

deleteAPI = Blueprint("deleteAPI", __name__)


@deleteAPI.route("/deleteEmp/<empId>", methods=["DELETE"])
def deleteEmp(empId):
    emp = Employee()
    emp.empId = empId
    emp.firstName = "DD"
    emp.lastName = "Mishra"
    return Response("Employee info deleted successfully", status=200, mimetype="plain/text")
