import streamlit as st
from chat import chat
import os

user_name = os.getenv('USER_NAME')
user_pass = os.getenv('USER_PASS')

def validate_login():
  if st.session_state.user == user_name and st.session_state.password == user_pass:
    st.session_state.authenticated = True
  else:
    st.session_state.authenticated = False
    st.error("ユーザー名かパスワードが無効です。")

def authenticate():
  if "authenticated" not in st.session_state:
    st.text_input(label="Username", value="", key="user")
    st.text_input(label="Password", value="", key="password")
    st.button(label="ログイン", on_click=validate_login)
    return False
  else:
    if st.session_state.authenticated:
      return True
    else:
      st.text_input(label="Username", value="", key="user")
      st.text_input(label="Password", value="", key="password")
      st.button(label="ログイン", on_click=validate_login)
      return False


if authenticate():
  chat()