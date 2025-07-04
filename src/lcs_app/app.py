import streamlit as st
from lcs_length import lcs_length

# ページ設定 ------------------------------------------------------------
st.set_page_config(page_title="LCS 長さ計算ツール", layout="centered")
st.title("🧮 最長共通部分列 (LCS) 長さ計算")

# 入力フォーム ----------------------------------------------------------
with st.form(key="lcs_form"):
    str1 = st.text_input("文字列 1", value="ABCDEF")
    str2 = st.text_input("文字列 2", value="ABBCCD")
    submitted = st.form_submit_button("計算する")

# 結果表示 --------------------------------------------------------------
if submitted:
    if str1 and str2:
        length = lcs_length(str1, str2)
        st.success(f"✅ LCS の長さ: **{length}**")
    else:
        st.warning("⚠️ どちらの文字列も空でないよう入力してください。")

st.markdown("---")
st.caption("Powered by Streamlit · 計算アルゴリズム: 動的計画法 (ローリング配列版)")
