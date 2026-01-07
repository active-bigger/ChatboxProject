"""
File: chat_main.py
Datetime: 2026/1/7 17:33
Author: ccy
Version: 1.0
Description:
该模块用于充当聊天机器人的前端模块，即：接收用户录入的问题，调用chat_utils模块的get_response函数，获取模型处理结果，
并通过streamlit在前端界面展示即可
"""
import os
import sys
import streamlit as st
from langchain.memory import ConversationBufferMemory  # ConversationBufferMemory：聊天记录存储器：存储所有聊天信息
from chat_utils import get_response

def main():
    st.title("智能聊天机器人")
    # 判断是否有历史消息记录对象，如果没有则创建，并存储所有的消息记录
    if 'memory' not in st.session_state: # st.session_state存储会话状态数据的字典，用于存储会话数据
        # 创建会话消息记录对象，并存储在st.session_state中
        st.session_state.memory = ConversationBufferMemory()
        # 添加机器人欢迎语
        st.session_state.messages = [{"role": "assistant", "content": "你好！我是智能聊天机器人，有什么可以帮助你的吗？"}]
    # 遍历 session_state.messages ,显示所有消息记录
    for message in st.session_state.messages:
        # message的格式 {"role": "assistant"或者"user" "content": "内容"}
        # 通过聊天消息容器，用于显示当前用户的内容
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # 接收用户录入的问题
    prompt = st.chat_input("请输入您的问题:")
    # 判断用户录入的问题不为空则继续进行
    if prompt:
        # 把用户的信息添加到历史消息记录中，并展示到前端
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)

        # 细节： 加入延时等待提示组件
        with st.spinner("AI小助理正在思考中..."):
            # 调用自定义的工具类chat_utils中的get_response函数，获取模型响应结果
            response = get_response(st.session_state.messages)

        # 把模型的处理结果添加到历史消息记录中，并展示到前端页面
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").markdown(response)



if __name__ == '__main__':
    main()
