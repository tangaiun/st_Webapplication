# 画像の挿入
import urllib.request as req
url = "https://betashort-lab.com/wp-content/uploads/2018/07/test.jpg"
req.urlretrieve(url, "test.jpg")

import streamlit as st

def Face1():
    st.title("Face1")
    st.image(url)

def Face2():
    st.title("Face2")


pages = dict(
    Face1="顔認識1",
    Face2="顔認識2",
)

page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
    "ページ名",
    ["Face1", "Face2"],
    format_func=lambda page_id: pages[page_id], # 描画する項目を日本語に変換
)

if page_id == "Face1":
    Face1()

if page_id == "Face2":
    Face2()