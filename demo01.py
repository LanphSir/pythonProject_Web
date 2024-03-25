import os
from urllib.parse import urljoin
import requests
from lxml import etree


def id_name1(ID_list, cname):
    if os.path.exists('picture'):
        pass
    else:
        os.mkdir('picture')
    resp = requests.get(ID_list)
    resp.encoding = resp.apparent_encoding
    curr = etree.HTML(resp.text)
    src = curr.xpath("//div[@class='zk-con1 zk-con']/@style")
    pic_pf = curr.xpath("//div[@class='pic-pf']/ul/@data-imgname")
    a = urljoin(ID_list, src[0].split("'")[1]).split('-1')
    j = 1
    for i in pic_pf[0].split("|"):
        if os.path.exists('picture/' + cname):
            pass
        else:
            os.mkdir('./picture/' + cname)
        if requests.get(f"{a[0] + '-' + str(j) + a[1]}").status_code == 200:
            a_liat = a[0] + '-' + str(j) + a[1]
            with open("./picture/" + cname + "/" + i + ".jpg", "wb") as f:
                f.write(requests.get(a_liat).content)
                print("下载好了", i)
            print(a_liat, cname, i)
        j += 1


def main(url):
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    for i in resp.json():
        yingxiong = f"https://pvp.qq.com/web201605/herodetail/{i['id_name']}.shtml"
        id_name1(yingxiong, i['cname'])


if __name__ == '__main__':
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    main(url)