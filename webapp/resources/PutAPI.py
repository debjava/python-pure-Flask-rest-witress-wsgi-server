import json
from types import SimpleNamespace

from webapp.services import EmployeeServices as empService
from flask import Blueprint, request, Response

putAPI = Blueprint("putAPI", __name__)

@putAPI.route("/updateEmp", methods=["PUT"])
def updateEmployee():
    jsonContent = request.get_json()
    print("Json Content from PUT request: ", jsonContent)
    jsonAsDict = json.dumps(jsonContent)
    empAsObject = json.loads(jsonAsDict, object_hook=lambda d: SimpleNamespace(**d))
    emp = empService.updateEmployee(empAsObject)
    empJson = json.dumps(emp.__dict__)
    return Response(response=empJson, status=201, mimetype="application/json")

