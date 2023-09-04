import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, AWS_S3_BUCKET

ALLOWED_EXTNESIONS={'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTNESIONS

def sessionAws():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION_NAME
        )
    return session

def upload_file(uploaded_file,newNameFile):
    try:
        if not allowed_file(uploaded_file.filename):
            raise ValueError("Only Image !")
        new_filename = newNameFile+'.'+uploaded_file.filename.rsplit('.',1)[1].lower()
        s3 = sessionAws().resource("s3")
        s3.Bucket(AWS_S3_BUCKET).upload_fileobj(uploaded_file,new_filename)
        return new_filename
    except Exception as e:
        raise ValueError("Cannot upload image")

    
def get_file(new_filename,ExpiresTime):
    try:
        s3_client = sessionAws().client('s3')
        url =  s3_client.generate_presigned_url('get_object',
                Params={
                    'Bucket': AWS_S3_BUCKET,
                    'Key': new_filename
                },
                ExpiresIn=ExpiresTime  # Số giây mà URL sẽ hết hạn
            )
        return url
    except Exception as e:
        raise ValueError("Cannot get image url")
        