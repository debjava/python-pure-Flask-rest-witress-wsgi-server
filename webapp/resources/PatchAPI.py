import json

from flask import Blueprint, request, Response

from webapp.entity.Employee import Employee

patchAPI = Blueprint("patchAPI", __name__)

@patchAPI.route("/updatePartialEmp", methods=["PATCH"])
def updatePartialInfo():
    qStr = request.query_string
    print("Query String in patch request: ", qStr)
    id = request.args.get("id")
    loginName = request.args.get("login")
    print("ID in patch request: ", id)
    print("Login Name in patch request: ", loginName)
    emp = Employee()
    emp.empId = id
    emp.firstName = loginName
    emp.lastName = "Mishra"
    empAsJson = json.dumps(emp.__dict__)
    return Response(empAsJson, status = 200, mimetype = "application/json")