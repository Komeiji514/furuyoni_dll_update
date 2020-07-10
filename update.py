# coding: UTF-8
import requests
import re
import os
import os.path

# download_url="http://47.105.173.19/furuyonibattle/download/SakuraArms_200602.dll"
download_url=""
webpage_url="http://47.105.173.19/furuyonibattle/log.html"
save_path="SakuraArms/SakuraArms.dll"
check_path="SakuraArms/CardData"
version=""

def get_download_url():
    flag1 = False   #url
    flag2 = False   #version
    req = requests.get(webpage_url)
    req.encoding = 'utf-8'

    if req.status_code == 404:
        print("404错误，无法连接到对战器日志页")
        print("对战器日志地址：")
        print("http://47.105.173.19/furuyonibattle/log.html")
        print("按回车键退出。")
        input()
        exit(0)
        
    pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
    html_text = req.text.split('\r\n')
    for line in html_text:
        if not flag1 and "最新dll" in line:
            # print(line)
            url_list = re.findall(pattern, line)
            # print('http://47.105.173.19/furuyonibattle/' + url_list[0][0])
            global download_url
            download_url = 'http://47.105.173.19/furuyonibattle/' + url_list[0][0]
            flag1 = True
        if not flag2 and "#对战器更新日志" in line:
            flag2 = True
        elif flag2:
            global version
            version = line.lstrip('#')
            break

    if flag1 == False:
        print("最新dll抓取失败！")
        print("按回车键退出。")
        input()
        exit(0)

    # with open('html.txt','wb') as f:
    #     f.write(req.text.encode())
    

def download():
    r = requests.get(download_url)
    while(True):
        try:
            with open(save_path,"wb") as f:
                f.write(r.content)
            print("最新dll抓取成功！版本："+version)
            #+"大小："+str(len(r.content))+"字节。"
            print("按回车键退出。")
            input()
            break
        except:
            print("写入文件%s失败。"%save_path)
            print("请关闭对战器后重试，或常世以管理员身份启动该程序。")
            print("按回车键重试。")
            input()

def check():
    if not os.path.exists(check_path):
        print("请将该程序放在对战器目录下，谢谢茄子！")
        print("按回车键退出。")
        input()
        exit(0)
    while(True):
        try:
            f = open(save_path,"rb+")
            f.close()
            break
        except:
            print("打开文件%s失败。"%save_path)
            print("请关闭对战器后重试，或常世以管理员身份启动该程序。")
            print("按回车键重试。")
            input()

if __name__ == '__main__':
    check()
    get_download_url()
    download()
