# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from UserDataModule.UserData import UserData
from firebase_functions import https_fn
from firebase_admin import initialize_app

initialize_app()


@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    temp = UserData("first name", 12, "email@email.com")
    print(temp)
    return https_fn.Response("Hello world!")