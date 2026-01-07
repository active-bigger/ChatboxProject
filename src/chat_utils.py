"""
File: chat_utils.py
Datetime: 2026/1/7 17:24
Author: ccy
Version: 1.0
Description:
该模块用于充当聊天机器人的后端模块，即：接收前端(Streamlit)传过来的用户的问题，
交给大语言模型，获取其响应结果，并返回（给前端）
"""
import os
import sys
from http.client import responses

import ollama
from click import prompt


# def get_response(prompt):
#     response = ollama.chat(model='deepseek-r1:1.5b',messages=[{"role":"user","content":prompt}])
#     result = response['message']['content']
#     return result

# 因为前端传过来的问题，是列表+字典的格式，已经符合OllamaAPI的格式，我们无需做处理
def get_response(prompt):
    response = ollama.chat(model='deepseek-r1:1.5b',messages=prompt[-50:]) # 取最近50个消息，避免超出上下文限制
    result = response['message']['content']
    return result



if __name__ == '__main__':
    prompt = "王者荣耀中的李白你认识吗？他有什么技能？"
    response = get_response(prompt)
    print(response)
