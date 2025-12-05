import flask
from google.cloud import storage
import functions_framework


BUCKET_NAME = "test_upload_backet"

@functions_framework.http
def upload_image(request: flask.Request) -> flask.typing.ResponseReturnValue:
    if request.method != "POST":
        return "Use POST method.", 405
    file = request.files.get("file")

    if file is None:
        return "No file uploaded.", 400
    
    storage_client = storage.Client()
    
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file, content_type=file.content_type)
    return f"Uploaded to gs://{BUCKET_NAME}/{file.filename}"