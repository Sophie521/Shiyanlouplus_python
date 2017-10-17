#!/usr/bin/env python3  #使用python3的解释器执行当前脚本
def char_count(str):
    char_list = set(str)
    for char in char_list:
        print(char,str.count(char))＃计算频次

if __name__ == '__main__':＃程序入口
    
    s=input("Enter a string:")

    char_count(s)
