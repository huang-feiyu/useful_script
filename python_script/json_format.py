#!/usr/bin/env python3
"""json格式化输出
author: Huang
date: 21.12.22
description: 给定json字符串数据，格式化输出
"""
import json

def print_json(data):
    """格式化输出函数，返回字典
    """
    # raw data转换为字典
    js_dic = json.loads(data)
    # 格式化输出
    print(json.dumps(js_dic, sort_keys=True, indent=4, separators=(',', ':')))
    return js_dic

def main():
    """主函数
    """
    temp_str = input("1. 测试\n2. raw data\n3. json文件绝对路径\n")
    if temp_str == '1':
        test_file = open('./resources/test.json', mode = 'r')
        raw_data = test_file.read()
        print_json(raw_data)
        test_file.close()
    elif temp_str == '2':
        raw_data = input("给定json数据:\n")
        print_json(raw_data)
    elif temp_str == '3':
        file_absolute_path = input("给定绝对路径:\n")
        rd_file = open(file_absolute_path, mode = 'r')
        raw_data = rd_file.read()
        print_json(raw_data)
        rd_file.close()
    else:
        print("再来一遍")
        main()


if __name__ == '__main__':
    main()
