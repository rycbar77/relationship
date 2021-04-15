import requests
from bs4 import BeautifulSoup
import re


def get_content(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36'
    }
    # url = "https://baike.baidu.com/item/%E4%BA%BA%E6%B0%91%E7%9A%84%E5%90%8D%E4%B9%89/17545218"
    res = requests.get(url, headers=header).text
    return res
    # print(res)


def get_intro(content):
    bs = BeautifulSoup(content, "lxml")
    intro = bs.find_all('ul', {'id': 'dramaSerialList'})
    intro = "".join([str(i) for i in intro])
    intro = re.sub(r'<[^>]+>', '', intro)
    # print(content)
    with open('./content.txt', 'w', encoding='utf-8') as f:
        f.write(intro)
    return intro


def get_name(content):
    bs = BeautifulSoup(content, "lxml")
    names = bs.find_all("dl", attrs={"class": "info"})
    chac = []
    for name in names:
        role = name.find_all("dt")
        for tag in role:
            tmp = tag.find_all("a")
            if tmp:
                tmp_name = re.sub(r"[（](.*)[）]", '',
                                  " ".join([i.get_text() for i in tmp]).replace('饰', '').replace('\xa0', ' ').split(
                                      ' ')[-1])
            else:
                tmp_name = re.sub(r"[（](.*)[）]", '',
                                  tag.get_text().replace('饰', '').replace('\xa0', ' ').split(' ')[-1])
            if "青年" in tmp_name:
                continue
            else:
                chac.append(tmp_name)
    with open('./name_dict.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(chac))


if __name__ == '__main__':
    url = "https://baike.baidu.com/item/%E4%BA%BA%E6%B0%91%E7%9A%84%E5%90%8D%E4%B9%89/17545218"
    content = get_content(url)
    get_intro(content)
    get_name(content)
