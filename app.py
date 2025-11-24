from dotenv import load_dotenv

load_dotenv()

#「app.py」にコードを記述してください。
#画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
#ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
#「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
#Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

st.title("専門家チャットアプリ")
st.write("このアプリでは、入力フォームにテキストを入力し、ラジオボタンで専門家の種類を選択して送信すると、選択した専門家としてLLMが回答します。")
def get_expert_response(user_input, expert_type):
    if expert_type == "医者":
        system_message = """あなたは優秀で親身な医者です。以下の指示に従って回答してください。

【回答の方針】
- 患者の不安な気持ちに寄り添い、優しく温かい言葉で回答する
- 専門用語は避け、素人にもわかりやすい言葉で説明する
- 必要に応じて具体例を挙げて説明する
- 患者を安心させるような配慮を心がける

【制約事項】
- 医療に関係のない質問には回答しない
- その場合は「申し訳ございませんが、医療に関する質問のみにお答えできます。」と返答する"""
    
    elif expert_type == "弁護士":
        system_message = """あなたは優秀で親身な弁護士です。以下の指示に従って回答してください。

【回答の方針】
- 相談者の不安な気持ちに寄り添い、優しく温かい言葉で回答する
- 法律用語は避け、素人にもわかりやすい言葉で説明する
- 必要に応じて具体例を挙げて説明する
- 相談者を安心させるような配慮を心がける

【制約事項】
- 法律に関係のない質問には回答しない
- その場合は「申し訳ございませんが、法律に関する質問のみにお答えできます。」と返答する"""
    
    else:
        system_message = "あなたは優秀な専門家です。質問に対して専門的かつ丁寧に回答してください。"

    chat = ChatOpenAI(temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]
    response = chat.invoke(messages)
    return response.content
user_input = st.text_input("質問を入力してください:")
expert_type = st.radio("専門家の種類を選択してください:", ("医者", "弁護士"))
if st.button("送信"):
    if user_input:
        answer = get_expert_response(user_input, expert_type)
        st.write("回答:")
        st.write(answer)
    else:
        st.write("質問を入力してください。") 

