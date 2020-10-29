import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = None


def init_browser():
    """
    init
    :return:
    """
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    global browser
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
    url = 'https://twitter.com/search?q=Singapore%20general%20election%202020&src=typed_query&f=live'
    #url = 'https://twitter.com/search?q=%23SGGE2020&src=typed_query&f=live'

    browser.get(url)
    time.sleep(5)


def parse_page():
    contents = []
    sel_month = ['Jun','Jul','Aug','May']
    try:
        texts = browser.find_elements(By.CSS_SELECTOR, ".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1mi0q7o")
        #css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0
        for t in texts:
            name = t.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1wbh5a2.r-dnmrzs')
            publish_time = t.find_element(By.CSS_SELECTOR,
                                          '.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0.css-4rbku5.css-18t94o4.css-901oao')
            publish_time_detail = publish_time.get_attribute('title')
            content = t.find_element(By.CSS_SELECTOR,
                                     ".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")

            transmit_and_like = t.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws')
            transmit_and_like_detail = transmit_and_like.get_attribute('aria-label')
            month = publish_time_detail.split(',')[0].split('·')[1]
            if  month.split(' ')[1].strip() in sel_month:
                transmit = '0'
                like = '0'
                if transmit_and_like_detail:
                    transmit_and_like_details = transmit_and_like_detail.split(', ')
                    for t_and_l in transmit_and_like_details:
                        print(t_and_l)
                        if 'reply' in t_and_l:
                            pass
                        elif 'Retweets' in t_and_l:
                            transmit = t_and_l.replace('Retweets', '').strip()
                        elif 'like' in t_and_l:
                            like = t_and_l.replace('like', '').strip()

                m = {'name': name.text, 'publish_time_detail': publish_time_detail, 'content': content.text,
                     'transmit': transmit, 'like': like}
                contents.append(m)
            else:
                print("NONE")
    except Exception as e:
        print(e)

    return contents


def save_content(content):
    """
    :param content: {'name': name.text, 'publish_time_detail': publish_time_detail, 'content': content.text,
                     'transmit': transmit, 'like': like}
    :return:
    """
    name = content.get('name')
    publish_time_detail = content.get('publish_time_detail')
    c = content.get('content')
    transmit = content.get('transmit')
    like = content.get('like')

    with open('twitter.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, publish_time_detail, c, transmit, like])

    s = name + publish_time_detail + '\n' + '------------------------' + '\n'
    with open('existing_contents.txt', 'a', encoding='utf-8') as f:
        f.write(s)

exist_contents = []


def load_exist_contents():
    exist_contents_file_path = 'existing_contents.txt'
    if os.path.exists(exist_contents_file_path):
        with open(exist_contents_file_path, 'r', encoding='utf-8') as f:
            strs = f.read()
            global exist_contents
            exist_contents = strs.split('------------------------')


def main():
    #load_exist_contents()
    init_browser()
    amount = 0
    scroll_amount = 0
    while amount < 1100:
        contents = parse_page()
        for content in contents:
            print('%d - Request' % amount)
            # name,publish_time_detail,content
            name = content.get('name')
            publish_time_detail = content.get('publish_time_detail')
            name_and_time = name + publish_time_detail
            if name_and_time not in exist_contents:
                exist_contents.append(name_and_time)
                amount += 1
                save_content(content)
            else:
                print('existings' + name_and_time)
        y = scroll_amount * 1000
        scroll_amount += 1
        browser.execute_script('window.scrollTo(0,' + str(y) + ')')
        time.sleep(5)


def test():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    global browser
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
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
