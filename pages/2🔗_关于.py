import streamlit as st
from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx
from streamlit.server.server import Server

st.set_page_config(
     page_title="关于",
     layout="wide",
     initial_sidebar_state="auto",
)

st.sidebar.title("欢迎使用我们为你制作的图像超分小工具♥️")

st.sidebar.markdown("---")
st.sidebar.success('"**_I hope this simple tool can help you better view pictures or videos_**."\n\n"**_If it can really bring you even a little help_**, **_it will be my greatest honor!_**"\n\n--**_All the members of the team_**')

st.balloons()

session_id = get_report_ctx().session_id
sessions = Server.get_current()._session_info_by_id
session_ws = sessions[session_id].ws
st.sidebar.info(f'当前在线人数：{len(sessions)}')

st.sidebar.write("---")
st.sidebar.caption("""You can check out the source code [here](https://github.com/JennieJisooBabe/Super_Resolution).""")
st.sidebar.caption("""You can access streamlit cloud share [here](https://xxxxxxxxxxxxx).""")
st.sidebar.write("---")

st.title('Thank you for your use and wish you all the best')
st.header('Hope you experience well.')
st.subheader('Following content also hopes you to know.')

st.header('网站制作者们🧑‍💻')
col1, col2, col3 = st.columns([2,2,2])
with col1:
   st.subheader("乔一鸣")
   st.image('qym.png',width=150)
   st.write("**from: 20软件一班**")
   st.write("**他没什么想说的......**")
with col2:
   st.subheader("何宇青")
   st.image('hyq.png',width=150)
   st.write("**from: 20大数据二班**")
   st.write("**大家好，我叫何宇青，我的名字是何宇青，现在给大家做自我介绍**\n\n**的是来自南京理工大学泰州科技学院的何宇青，希望大家能记住我叫何宇青。**")
with col3:
   st.subheader("罗怡纯")
   st.image('lyc.png',width=150)
   st.write("**from: 20软件一班**")
   st.write("**只管走过去，不必逗留着采了花朵来保存，因为一路上花朵自会继续开放的。**")
col4, col5, col6 = st.columns([2,2,2])
with col4:
   st.subheader("张钰娟")
   st.image('zyj.png',width=150)
   st.write("**from: 21软嵌班**")
   st.write("**超级无敌大帅哥**")
with col5:
   st.subheader("王政豪")
   st.image('wzh.png',width=150)
   st.write("**from: 20计二班**")
   st.write("**人生只有贪心，没有动态规划。**")
with col6:
   st.subheader("冯意")
   st.image('fy.png',width=150)
   st.write("**from: 20计二班**")
   st.write("**兴趣爱好：编程，羽毛球，音乐。**")

st.header('超分算法原引📋')
st.subheader('使用高效的亚像素卷积神经网络实现实时单图像和视频超分辨率')
st.caption('https://arxiv.org/pdf/1609.05158.pdf')
st.subheader('加速超分辨率卷积神经网络')
st.caption('http://mmlab.ie.cuhk.edu.hk/projects/FSRCNN.html')
st.subheader('深度拉普拉斯金字塔网络实现快速准确的超分辨率')
st.caption('https://arxiv.org/pdf/1704.03915.pdf')
st.subheader('增强的深度残差网络实现单图像超分辨率')
st.caption('https://arxiv.org/pdf/1707.02921.pdf')

# from streamlit_disqus import st_disqus
#
# st_disqus("streamlit-disqus-demo")

st.warning('欢迎通过左侧的链接访问github源码与我们一起将它改良完善。')
st.warning('有任何问题可在评论区留言，我们在看到后会第一时间为您解决。')