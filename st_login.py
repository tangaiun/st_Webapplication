
import streamlit as st

st.title("Counter Example")

# セッションステートを初期化
if "count" not in st.session_state:
    st.session_state.count0 = 0

# "Increment"ボタンを表示し、押されたかどうかを取得
increment = st.button("Increment")

# もしボタンが押された場合
if increment:
    # セッションステートのカウンターを1増やす
    st.session_state.count1 += 1

# セッションステートのカウンターの値を表示
st.write("Count = ", st.session_state.count1)
