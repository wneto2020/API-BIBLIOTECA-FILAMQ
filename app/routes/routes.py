from app import app
from app.views import users


@app.route("/obras", methods=["POST"])
def insert_obras():
    return users.insert_obras()


@app.route("/upload-obras", methods=["POST"])
def upload_obras():
    return users.upload_obras()


@app.route("/obras/", methods=["GET"])
def return_obras():
    return users.return_obras()


@app.route("/obras/<id>", methods=["PUT"])
def update_obras(id):
    return users.update_obras(id)


@app.route("/obras/<id>", methods=["DELETE"])
def delete_obras(id):
    return users.delete_obras(id)


@app.route("/file-obras/", methods=["POST"])
def request_email():
    return users.request_email()