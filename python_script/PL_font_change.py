#!/usr/bin/env python3
"""更换字体 for terminal Ligatures
author: Huang
date: 22.2.18
"""
import re

USERNAME = '36542'

def which_font(lines, line_num):
  """根据现有的字符更改数据
  """
  lookup_Fira_Code = re.compile(r'.+Fira Code.+$') # for code
  lookup_MesloLGS_NF = re.compile(r'.+MesloLGS NF.+$') # for shell
  if (re.search(lookup_Fira_Code, lines[line_num - 4])):
    lines[line_num - 4] = """                    "face": "MesloLGS NF",\n"""
    print("MesloLGS NF")
    return lines
  if (re.search(lookup_MesloLGS_NF, lines[line_num - 4])):
    lines[line_num - 4] = """                    "face": "Fira Code",\n"""
    print("Fira Code")
  else:
    print("sth went wrong")
  return lines

def main():
    """主函数
    """
    setting_file_path = '/mnt/c/Users/' + USERNAME +\
    '/AppData/Local/Packages/Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe/LocalState/settings.json'
    lookup = re.compile(r'.+07b52e3e-de2c-5db4-bd2d-ba144ed6c273.+$') # guid
    # 找到行号
    line_num = 0
    lines = []
    with open(setting_file_path) as my_file:
        lines = my_file.readlines()
        lines_length = len(lines)
        for num in range(lines_length):
            if re.search(lookup, lines[num]):
                line_num = num
    # cause everything in `settings.json` is ordered
    lines = which_font(lines, line_num)
    with open(setting_file_path, 'w') as my_file:
        for data in lines:
            my_file.write(data)
        my_file.flush()

if __name__ == '__main__':
    main()
