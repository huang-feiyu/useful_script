#!/usr/bin/env python3
"""获取每天bing壁纸，并且更新windows terminal settings
author: Huang
date: 21.12.22
"""
import re
import json
from urllib.request import urlopen

USERNAME = '36542'

def get_url():
    """获取壁纸url
    """
    bing_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    bing_api = urlopen(bing_url)
    raw_bytes = bing_api.read()
    raw_json = str(raw_bytes, encoding='utf-8')
    dic = json.loads(raw_json)
    print(re.search(r"id=OHR\.((.*?))_", dic['images'][0]['url'])[1])
    return '"' + "https://bing.com" + dic['images'][0]['url'] + '"'

def main():
    """主函数
    """
    setting_file_path = '/mnt/c/Users/' + USERNAME +\
    '/AppData/Local/Packages/Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe/LocalState/settings.json'
    lookup = re.compile(r'.+https:\/\/bing\.com.+$')
    # 找到行号
    line_num = 0
    lines = []
    with open(setting_file_path) as my_file:
        lines = my_file.readlines()
        lines_length = len(lines)
        for num in range(lines_length):
            if re.search(lookup, lines[num]):
                line_num = num
    lines[line_num] = """                    "backgroundImage": """ + get_url() + '\n'
    with open(setting_file_path, 'w') as my_file:
        for data in lines:
            my_file.write(data)
        my_file.flush()

if __name__ == '__main__':
    main()
