from config import MINIO_CONFIG, MYSQL_CONFIG
from mappertool.miniotools import MinioUploader
from mappertool.redis_singleton import RedisCache
from crawl.crawlwebsite import crawl_website
from mappertool.sqlmysqlsaveinfo import DatabaseManager
from utiltool.movepicture import move_images_to_dir


class CrawlManager:
    def __init__(self, taskid):
        self.redis_conn = RedisCache()
        self.minio_config = MINIO_CONFIG
        self.mysql_config = MYSQL_CONFIG
        self.queue_name = taskid + "_queue"
        self.website_hash = taskid + "_queuehash"
        self.init_queue_and_hash()

    def init_queue_and_hash(self):
        websites = [
            "https://baidu.com/",
            "https://gwozai.com/",
            "https://163.com",
            "https://white-plus.net/thread.php",
            "https://blog.csdn.net/",
            "https://bbs.imoutolove.me/",
            "https://gmgard.moe/",
        ]

        for website in websites:
            self.redis_conn.enqueue(self.queue_name, website)
        self.redis_conn.set_hash_data(self.website_hash, "None", "0")

    def proceed(self):

            move_images_to_dir()
            result = self.redis_conn.dequeue(self.queue_name)
            decoded_str = result["result"].decode("utf-8")
            if self.redis_conn.exists_hash_data(self.website_hash, decoded_str)["result"]:
                return
            infos = crawl_website(decoded_str)
            if infos is not None:
                self.process_website(infos, decoded_str)

    def process_website(self, infos, decoded_str):
        print("正在抓取...: {0}".format(decoded_str))
        website_url, title, h1, links_set, screenshot_path = infos
        minio_uploader = MinioUploader(
            endpoint=self.minio_config["endpoint"],
            access_key=self.minio_config["access_key"],
            secret_key=self.minio_config["secret_key"],
            secure=self.minio_config["secure"],
        )
        minio_path = minio_uploader.upload_file(self.minio_config["bucket"], screenshot_path)

        for link in links_set:
            self.redis_conn.enqueue(self.queue_name, link)

        print(self.redis_conn.set_hash_data(self.website_hash, website_url, "0"))
        print("Website URL:", website_url)
        print("Title:", title)
        print("H1 Titles:", h1)
        print("Distinct Link Domains:", links_set)
        print("Screenshot Path:", screenshot_path)
        print("Minio Path:", minio_path)

        data = {
            "website_url": website_url,
            "title": title,
            "h1_titles": h1,
            "distinct_link_domains": links_set,
            "screenshot_path": screenshot_path,
            "minio_path": minio_path,
        }

        db_manager = DatabaseManager(
            self.mysql_config["host"],
            self.mysql_config["dbname"],
            self.mysql_config["user"],
            self.mysql_config["password"],
        )
        db_manager.connect()
        result = db_manager.save_to_database(data)
        print(result)
        db_manager.close()


# if __name__ == "__main__":
#     taskid = "taskidtest"
#     crawl_manager = CrawlManager(taskid)
#     crawl_manager.proceed()