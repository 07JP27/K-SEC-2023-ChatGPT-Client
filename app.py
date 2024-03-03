import streamlit as st
import streamlit_authenticator as sa
from chat import chat
import os

#ページタイトルとアイコンを設定する。
st.set_page_config(page_title="K-SEC 2023 ChatGPT ハンズオンアプリ", page_icon="💬",layout="wide")

user_name = os.getenv('USER_NAME')
user_pass = os.getenv('USER_PASS')

authenticator = sa.Authenticate(
    credentials={"usernames":{
      user_name:{"name":user_name,"password":user_pass}
    }},
    cookie_name="streamlit_cookie",
    key="signature_key",
    cookie_expiry_days=1
)

authenticator.login()

if st.session_state["authentication_status"] is False: #ログイン失敗
  st.error('ユーザー名かパスワードが無効です。')
elif st.session_state["authentication_status"] is None: #未入力
  st.warning('ユーザー名とパスワードを入力してください。')
else: #ログイン成功
  chat()
  authenticator.logout(location="sidebar") 
