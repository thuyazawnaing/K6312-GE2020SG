import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = None


def init_browser():
    """
    初始化浏览器
    :return:
    """
    # 这里！！！！实现不关闭的重点
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    global browser
    browser = webdriver.Chrome(executable_path='/Applications/chromedriver', options=option)
    # 热门的
    # url = 'https://twitter.com/search?q=Singapore%20general%20election&src=typed_query'
    # 最新的
    url = 'https://twitter.com/search?q=Singapore%20general%20election&src=typed_query&f=live'
    browser.get(url)
    time.sleep(5)


def parse_page():
    """
    解析网页
    :return:
    """
    contents = []
    try:
        texts = browser.find_elements(By.CSS_SELECTOR, ".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1mi0q7o")
        # 内容css：css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0
        for t in texts:
            name = t.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1wbh5a2.r-dnmrzs')
            publish_time = t.find_element(By.CSS_SELECTOR,
                                          '.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0.css-4rbku5.css-18t94o4.css-901oao')
            publish_time_detail = publish_time.get_attribute('title')
            content = t.find_element(By.CSS_SELECTOR,
                                     ".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")
            month = publish_time_detail.split('年')[1]
            description = t.find_element(By.CSS_SELECTOR, ",css-1dbjc4n r-aqfbo4 r-1p0dtai r-1d2f490 r-12vffkv r-1xcajam r-zchlnj")
            if '6月' in month or '7月' in month or '8月' in month:
                m = {'name': name.text, 'publish_time_detail': publish_time_detail, 'content': content.text, 'description': description.text}
                contents.append(m)
    except Exception as e:
        print(e)

    return contents


def save_content(content):
    """
    保存内容
    :param content: {'name': name.text, 'publish_time_detail': publish_time_detail, 'content': content, 'description': description.text}
    :return:
    """
    name = content.get('name')
    publish_time_detail = content.get('publish_time_detail')
    c = content.get('content')
    description = content.get ('description')
    
    with open('twitter.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, publish_time_detail, c, description])

    s = name + publish_time_detail + '\n' + '------------------------' + '\n'
    with open('已经存在的内容.txt', 'a', encoding='utf-8') as f:
        f.write(s)


# 已经存在的内容
exist_contents = []

def load_exist_contents():

    exist_contents_file_path = '已经存在的内容.txt'
    if os.path.exists(exist_contents_file_path):
        with open(exist_contents_file_path, 'r', encoding='utf-8') as f:
            strs = f.read()
            global exist_contents
            exist_contents = strs.split('------------------------')


def main():
    load_exist_contents()
    init_browser()
    amount = 0
    scroll_amount = 0
    while amount < 1100:
        contents = parse_page()
        for content in contents:
            print('第次%d请求' % amount)
            # name,publish_time_detail,content
            name = content.get('name')
            publish_time_detail = content.get('publish_time_detail')
            name_and_time = name + publish_time_detail
            if name_and_time not in exist_contents:
                exist_contents.append(name_and_time)
                amount += 1
                # 保存到内容到文件中
                save_content(content)
            else:
                print('已经存在' + name_and_time)

        y = scroll_amount * 1000
        scroll_amount += 1
        browser.execute_script('window.scrollTo(0,' + str(y) + ')')
        time.sleep(5)


def test():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    global browser
    browser = webdriver.Chrome(executable_path='/Applications/chromedriver', options=option)
    url = 'http://163.com/'
    browser.get(url)
    a = 0
    while a < 10:
        a += 1
        y = a * 1000
        browser.execute_script('window.scrollTo(0,' + str(y) + ')')
        print(a)


if __name__ == '__main__':
    main()
    # test()
    # load_exist_contents()
    # print(len(exist_contents))
    
    
