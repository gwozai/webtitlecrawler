from crawl_and_process_websites import CrawlManager

if __name__ == "__main__":
    taskid = "taskidtest"
    crawl_manager = CrawlManager(taskid)
    crawl_manager.proceed()