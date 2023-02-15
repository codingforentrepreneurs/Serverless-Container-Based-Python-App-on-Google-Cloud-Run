# import google-auth
import google.auth
try:
    _, project_id = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    project_id = None
print(project_id)


if project_id is not None:
    # import google-cloud-secret-manager
    from google.cloud import secretmanager


    client = secretmanager.SecretManagerServiceClient()
    # my_secret_file is the name of the secret you
    # set with `gcloud secrets create ....`
    secret_label = "py_env_file"

    # project_id comes from previous step
    gcloud_secret_name = f"projects/{project_id}/secrets/{secret_label}/versions/latest"

    # this should print the contents of your secret
    payload = client.access_secret_version(name=gcloud_secret_name).payload.data.decode("UTF-8")

    # print the contents
    print(payload)
    print(payload.get("MODE"))
