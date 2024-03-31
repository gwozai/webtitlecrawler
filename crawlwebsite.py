from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

def get_domain(url):
    if url is None or url.startswith('javascript:'):
        return None
    result = urlparse(url)
    if result.scheme and result.netloc:
        return f'{result.scheme}://{result.netloc}'
    else:
        return None

def crawl_website(website_url):
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context()
            page = context.new_page()

            page.goto(website_url)
            website_url_name = website_url.replace('https://', '').replace('.', '_')

            title = page.title()

            h1 = [element.inner_text() for element in page.query_selector_all("h1")]

            links_set = {get_domain(link.get_attribute("href")) for link in page.query_selector_all("a")}
            website_url_name = website_url.replace('https://', '').replace('http://', '').replace('.', '_').replace(':',
                                                                                                                    '').replace(
                '/', '')
            screenshot_path = website_url_name + ".png"
            page.screenshot(path=screenshot_path, full_page=True)
            browser.close()

            return website_url, title, h1, links_set, screenshot_path
    except Exception as e:
        print(e)
        return None