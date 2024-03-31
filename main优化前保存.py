from crawlwebsite import crawl_website
from miniotools import MinioUploader
import os
from redis_singleton import RedisCache
from sqlmysqlsaveinfo import DatabaseManager
from 移动图片 import move_images_to_dir

if __name__ == "__main__":
    RedisCache().enqueue("addqueqe", "https://baidu.com/")
    RedisCache().enqueue("addqueqe", 'https://gwozai.com/')
    RedisCache().enqueue("addqueqe", 'https://163.com')
    RedisCache().enqueue("addqueqe", 'https://white-plus.net/thread.php')
    RedisCache().enqueue("addqueqe", 'https://blog.csdn.net/')
    RedisCache().enqueue("addqueqe", 'https://bbs.imoutolove.me/')
    RedisCache().enqueue("addqueqe", 'https://gmgard.moe/')
    hash_data = "websit_hashdata"

    print(RedisCache().set_hash_data(hash_data, "None", "0"))

    while True:
        move_images_to_dir()
        result = RedisCache().dequeue("addqueqe")
        decoded_str = result['result'].decode('utf-8')
        hash_data_exists = RedisCache().exists_hash_data(hash_data, decoded_str)
        if hash_data_exists['result']:
            continue


        infos = crawl_website(decoded_str)
        if infos is not None:
            print(f'正在抓取...: {decoded_str}')
            website_url, title, h1, links_set, screenshot_path = infos

            minio_uploader = MinioUploader(
                endpoint='1.15.7.2:9000',
                access_key='lizhuo',
                secret_key='1906014138',
                secure=False
            )
            minio_path = minio_uploader.upload_file("ooo", screenshot_path)
            for i in  links_set:
                RedisCache().enqueue("addqueqe", i)

            print(RedisCache().set_hash_data(hash_data, website_url, "0"))
            print("Website URL:", website_url)
            print("Title:", title)
            print("H1 Titles:", h1)
            print("Distinct Link Domains:", links_set)
            print("Screenshot Path:", screenshot_path)
            print("Minio Path:", minio_path)

            data = {
                'website_url': website_url,
                'title': title,
                'h1_titles': h1,
                'distinct_link_domains': links_set,
                'screenshot_path': screenshot_path,
                'minio_path': minio_path
            }

            db_manager = DatabaseManager('1.15.7.2', 'website', 'Yd6XjJswwJZaKEmb', 'website')
            db_manager.connect()
            result = db_manager.save_to_database(data)
            print(result)
            db_manager.close()