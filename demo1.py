import streamlit as st
import time
#st.write('hello world') #write

#st.markdown("man!")  #markdown

#st.markdown("# man!")  #markdown title

#st.markdown("> man!")  #markdown 

#st.code('iiiiiiii') #代码段

#st.video('https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/751bf7071397757901511609911/v.f100830.mp4')
#播放视频url

#sex = st.text_input('输入性别', max_chars=5, help='最大长度为5字符') #字符输入

#st.write('您的性别是',sex) #字符输出

#age = st.number_input('年龄',1,10,6) #数字输入

#st.write(f'input sex is {sex}, age is {age}')
#st.write("sex and age", sex,age)
#st.write("sex and age", age,sex)

def mock_login(username, pwd):
    time.sleep(3)
    return username == 'a' and pwd == '123'
#button

#登录页面
username = st.text_input('username','admin')
password = st.text_input('password', '114514')

if st.button("login"):
    with st.spinner('loading......'):
        login_result = mock_login(username, password)
        text = '登录成功' if login_result else '登录失败'
        st.write(text)