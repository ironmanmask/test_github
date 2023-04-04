import requests
from bs4 import BeautifulSoup as bs

ALLU = []


def readHTML(url):
    try:
        web = requests.get(url, timeout=30)
        web.raise_for_status()
        web.encoding = 'utf-8'
        return web.text
    except:
        return 0


def classify(soup, str):
    flag = 0
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleU = []
        for td in ltd:
            singleU.append(td.text.split())
        for i in singleU:
            for item in i:
                if item == str:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                break
        if flag == 1:
            ALLU.append(singleU)
            flag = 0


def output(num):
    print("{1:{0}^5}{2:{0}^20}{3:{0}^6}{4:{0}^4}{5:{0}^10}".format(
        chr(12288), "排名", "学校名称", "省市", "类型", "总分"))
    try:
        for i in range(num):
            u = ALLU[i]
            if u[0][0] == '2022排名':
                continue
            elif u[0][0][0].isdigit():
                print("{1:^10}{2:{0}^20}{3:{0}^6}{4:{0}^4}".format(
                    chr(12288), u[0][0], u[1][0], u[2][0], u[3][0]),
                      end="")
            else:
                print("{1:{0}^10}{2:{0}^15}{3:{0}^10}{4:{0}^1}".format(
                    chr(12288), u[0][0], u[1][0], u[2][0], u[3][0]),
                      end="")

            try:
                print("{0:^20}".format(u[4][0]))
            except:
                print('')
                continue
    except:
        print("已输出达上限")


def main(num):
    str1 = input("请输入查询省份")
    url = "https://www.hangge.com/blog/cache/detail_3187.html"
    webt = readHTML(url)
    process = bs(webt, "html.parser")
    classify(process, str1)

    fp = open("Urange.txt", "w")
    for line in ALLU:
        for lie in line:
            try:
                fp.write(lie[0])
            except:
                continue
        fp.write('\n')

    fp.close()
    output(num)


main(100)
