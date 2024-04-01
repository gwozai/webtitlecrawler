def singleton(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


import minio
import os

CONTENT_TYPES = {
    '.txt': 'text/plain',
    '.html': 'text/html',
    '.json': 'application/json',
    '.xml': 'application/xml',
    '.jpeg': 'image/jpeg',
    '.jpg': 'image/jpeg',
    '.png': 'image/png',
    '.mp3': 'audio/mpeg',
    '.mpeg': 'audio/mpeg',
    '.mp4': 'video/mp4',
    '.pdf': 'application/pdf'
}
# minio_config = {
#     'endpoint': 'play.minio.io:9000',  # 这只是一个样例endpoint，你需要替换成你自己的minio server地址
#     'access_key': 'YOUR-ACCESS-KEY',  # 你的access key
#     'secret_key': 'YOUR-SECRET-KEY',  # 你的secret key
#     'secure': False,  # 是否使用HTTPS，如果你的server支持的话，建议设置为True
# }

@singleton
class MinioUploader:
    def __init__(self, endpoint, access_key, secret_key, secure=False):
        self.endpoint = endpoint
        self.client = minio.Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )

    def get_content_type(self, file_path):
        extension = os.path.splitext(file_path)[1].lower()
        return CONTENT_TYPES.get(extension, 'application/octet-stream')

    def upload_file(self, bucket, file_path):
        if not os.path.isfile(file_path):
            return None
        try:
            object_name = os.path.basename(file_path)
            content_type = self.get_content_type(file_path)
            self.client.fput_object(
                bucket_name=bucket,
                object_name=object_name,
                file_path=file_path,
                content_type=content_type,
            )
            img_url = f'http://{self.endpoint}/{bucket}/{object_name}'
            return img_url
        except Exception:
            return None