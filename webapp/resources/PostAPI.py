import json
from types import SimpleNamespace

from flask import Blueprint, request, Response
from webapp.entity.Employee import Employee
from webapp.services import EmployeeServices as empService

postAPI = Blueprint("postAPI", __name__)


# Using employee as json localhost:8090/createEmp
@postAPI.route('/createEmp', methods=["POST"])
def createEmployee():
    jsonContent = request.get_json()
    print("Json Content from POST request: ", jsonContent)
    jsonAsDict = json.dumps(jsonContent)
    empAsObject = json.loads(jsonAsDict, object_hook=lambda d: SimpleNamespace(**d))
    empService.createEmployee(empAsObject)
    # return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    return Response(response="Employee created successfully", status=201, mimetype="application/json")
    # r.headers["Content-Type"] = "text/xml; charset=utf-8"


# Using form parameter
@postAPI.route("/saveEmp", methods=["POST"])
def saveEmp():
    id = request.form.get("id")
    print("Id: ", id)
    firstName = request.form.get("fName")
    print("firstName: ", firstName)
    lastName = request.form.get("lName")
    print("lastName: ", lastName)
    emp = Employee()
    emp.empId = id
    emp.firstName = firstName
    emp.lastName = lastName
    print("Employee as object: ", emp)
    return Response("Employee info saved successfully", status=200, mimetype="plain/text")


@postAPI.route("/createEmpKey", methods=["POST"])
def createEmployeeKey():
    #     key = request.headers["key"] # It is also possible
    key = request.headers.get("key")
    print("Accepted Key: ", key)
    jsonContent = request.get_json()
    jsonAsDict = json.dumps(jsonContent)
    empAsObject = json.loads(jsonAsDict, object_hook=lambda d: SimpleNamespace(**d))
    empService.createEmployee(empAsObject)
    return Response(response="Employee created successfully", status=201, mimetype="plain/text")
