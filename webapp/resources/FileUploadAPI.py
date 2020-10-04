import json
import os
from types import SimpleNamespace
from webapp.services import EmployeeServices as empService
from flask import Blueprint, request, Response
from werkzeug.utils import secure_filename

fileUploadAPI = Blueprint("fileUploadAPI", __name__)

UPLOAD_FOLDER = "E:\sure-delete"


@fileUploadAPI.route("/singleFile", methods=["POST"])
def uploadSingleFile():
    uploadedFile = request.files['file']
    filename = secure_filename(uploadedFile.filename)
    print("Uploaded File Name: ", filename)
    resText = "File with file name " + filename + " uploaded successfully"
    uploadedFile.save(os.path.join(UPLOAD_FOLDER, filename))
    return Response(resText, status=200, mimetype="plain/text")


@fileUploadAPI.route("/multipleFiles", methods=["POST"])
def uploadMultipleFiles():
    uploadedFiles = request.files.getlist("file")
    for file in uploadedFiles:
        print("File Name: ", file.filename)
        file.save(os.path.join(os.path.join(UPLOAD_FOLDER), file.filename))
    return Response("All files uploaded successfully", status=200, mimetype="plain/text")


@fileUploadAPI.route("/uploadEmpProfile", methods=["POST"])
def uploadEmpProfile():
    uploadedFile = request.files['file']
    filename = secure_filename(uploadedFile.filename)
    print("Uploaded File Name: ", filename)
    uploadedFile.save(os.path.join(UPLOAD_FOLDER, filename))
    empInfoJsonStr = request.form.get("empInfo")
    print("Emp Info as json String: ", empInfoJsonStr)
    empAsObject = json.loads(empInfoJsonStr, object_hook=lambda d: SimpleNamespace(**d))
    empObj = empService.createEmployee(empAsObject)
    empJsonString = json.dumps(empObj.__dict__)
    return Response(empJsonString, status=200, mimetype="application/json")
