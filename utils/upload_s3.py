import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, AWS_S3_BUCKET,EXPIRES_TIME,S3_ENDPOINT
from datetime import datetime
import traceback

ALLOWED_EXTNESIONS={'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTNESIONS

s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    use_ssl=False,
)

def upload_image_url(file,newNameFile):
        try:

            if not allowed_file(file.filename):
                raise ValueError("Only Image !")
            
            cur_date = datetime.today().strftime('%Y/%m/%d')
            name_prefix = int(datetime.today().timestamp())

            _filename = str(newNameFile)

            key_path_upload = f'admin_panel/{cur_date}/{name_prefix}_{_filename}.{file.filename.split(".")[-1]}'
            s3.upload_fileobj(
                file,
                AWS_S3_BUCKET,
                key_path_upload,
                ExtraArgs={
                    "ContentType": file.content_type  # Set appropriate content type as per the file
                }
            )
        except Exception as e:
            traceback.print_exc()
            return e
        return f'https://{AWS_S3_BUCKET}/{key_path_upload}'

        