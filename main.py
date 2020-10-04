from flask import Flask
from waitress import serve

from webapp.resources.DeleteApi import deleteAPI
from webapp.resources.FileDownloadAPI import fileDownloadAPI
from webapp.resources.FileUploadAPI import fileUploadAPI
from webapp.resources.GetAPI import getAPI
from webapp.resources.PatchAPI import patchAPI
from webapp.resources.PostAPI import postAPI
from webapp.resources.PutAPI import putAPI

app = Flask(__name__)

app.register_blueprint(getAPI, url_prefix="/myapp")
app.register_blueprint(postAPI, url_prefix="/myapp")
app.register_blueprint(putAPI, url_prefix="/myapp")
app.register_blueprint(patchAPI, url_prefix="/myapp")
app.register_blueprint(deleteAPI, url_prefix="/myapp")
app.register_blueprint(fileUploadAPI, url_prefix="/myapp")
app.register_blueprint(fileDownloadAPI, url_prefix="/myapp")

if __name__ == "__main__":
    # Using witress server
    serve(app, host='0.0.0.0', port=8090)
