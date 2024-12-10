from icrawler.builtin import GoogleImageCrawler


def download_images(path: str, word: str, count: int):
    """
    скачиваем фото по слову
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': path}, 
        feeder_threads=2,
        parser_threads=2,
        downloader_threads=5)

    google_crawler.crawl(keyword=word, max_num=count)
    print("Done!\n")
