from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential
import streamlit as st
#import streamlit_antd_components as sac
import os

def chat():
    #ページタイトルとアイコンを設定する。
    st.set_page_config(page_title="K-SEC 2023 ChatGPT ハンズオンアプリ", page_icon="💬",layout="wide")

    #タイトルを表示する。
    st.markdown("## K-SEC 2023 ChatGPT ハンズオンアプリ")

    #サイドバーに説明を表示する。
    st.sidebar.header("設定画面")

    st.sidebar.selectbox("Model", ("gpt-35-A","gpt-35-B","gpt-35-C","gpt-35-D","gpt-35-E","gpt-35-F","gpt-35-G","gpt-35-H","gpt-35-I","gpt-35-J","gpt-35-K","gpt-35-L","gpt-35-M","gpt-35-M","gpt-35-N","gpt-35-Spare"), key="deployment")
    st.sidebar.text_area("System Prompt", value="You are an AI chatbot having a conversation with a human.",key="system_prompt")
    if st.sidebar.button('Set system Prompt',  use_container_width=True):
        st.session_state.messages = [{"role":"system", "content":st.session_state.system_prompt}]
        st.session_state.Clear = False 
        st.rerun()
    st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, key="temperature")
    st.sidebar.slider("Max_Tokens(最大応答トークン数)", 0, 2048, 500, 1, key="max_tokens")

    default_credential = DefaultAzureCredential()
    token = default_credential.get_token("https://cognitiveservices.azure.com/.default")
    base = os.getenv('OPENAI_API_ENDPOINT')
    api_version = os.getenv('OPENAI_API_VERSION')
    client = AzureOpenAI(
        azure_endpoint = base, 
        azure_ad_token=token.token,
        api_version=api_version
    )

    if "deployment" not in st.session_state:
        st.session_state["deployment"] = "gpt-35-4"

    if "Clear" not in st.session_state:
        st.session_state.Clear = False
   
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7

    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 500
    
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You are an AI chatbot having a conversation with a human."

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"system", "content":st.session_state.system_prompt}]
       
    for message in st.session_state.messages:
        if not message["role"]=="system":
            if message["role"]=="user":
                with st.chat_message(message["role"], avatar = "😊"):
                    st.markdown(message["content"])
            elif message["role"]=="assistant":
                with st.chat_message(message["role"], avatar = "🤖"):
                    st.markdown(message["content"])

    if prompt := st.chat_input("ここに入力"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar = "😊"):
            st.markdown(prompt)

        with st.chat_message("assistant" , avatar = "🤖"):
            message_placeholder = st.empty()
            response = client.chat.completions.create(
                model=st.session_state["deployment"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            full_response =response.choices[0].message.content
            message_placeholder.markdown(full_response)
            st.sidebar.header("利用トークン数")
            st.sidebar.write('トータルトークン数：', str(response.usage.total_tokens))
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.session_state.Clear = True

    if st.session_state.Clear:
        if st.button('clear chat history'):
            st.session_state.messages = []
            full_response = ""
            st.session_state.total_tokens = 0
            st.session_state.Clear = False 
            st.rerun()

if __name__ == "__main__":
    chat()