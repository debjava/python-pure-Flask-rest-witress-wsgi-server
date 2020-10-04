import os

from flask import Blueprint, send_file, send_from_directory

fileDownloadAPI = Blueprint("fileDownloadAPI", __name__)

UPLOAD_FOLDER = "E:\sure-delete"


@fileDownloadAPI.route("/download/<filename>", methods=["GET"])
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)


@fileDownloadAPI.route("/showImage/<filename>", methods=["GET"])
def downloadFromDirectory(filename):
    uploads = os.path.join(UPLOAD_FOLDER)
    return send_from_directory(directory=uploads, filename=filename)
