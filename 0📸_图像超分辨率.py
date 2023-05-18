import os
import cv2
import numpy as np
import streamlit as st
from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx
from streamlit.server.server import Server
from streamlit_image_comparison import image_comparison
from algorithm import *

st.set_page_config(
     page_title="图像超分辨率",
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
st.sidebar.caption("""You can access streamlit cloud share [here](https://jenniejisoobabe-super-resolution-0--9hs3ti.streamlit.app/).""")
st.sidebar.write("---")

def is_im(file_name):
  suffix = file_name.split('.')[-1]
  if suffix in ['png', 'jpg','JPG', 'jpeg', 'gif']:
    return True
  return False

st.title('图像超分辨率')

uploaded_file = st.file_uploader("请上传图片文件")
if uploaded_file is not None:
    file_name = uploaded_file.name
    if is_im(file_name):
      bytes_data = uploaded_file.getvalue()

      try:
        im = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        img_result = cv2.resize(im,(0,0),fx=0.3,fy=0.3)
        img111 = cv2.cvtColor(img_result,cv2.COLOR_BGR2RGB)
        st.image(img_result, channels="BGR",width=600)
      except Exception:
        e = RuntimeError('文件上传出错，请重试！')
        st.exception(e)
      st.write('图片尺寸')
      st.write(im.shape)

      option = st.selectbox(
          '选择你需要的算法',
          ('最近邻插值算法', '双线性插值算法','双三次插值算法',
          'ESPCN深度学习算法', 'FSRCNN深度学习算法' , 'AttnSRCNN深度学习算法'))

      if option in ['ESPCN深度学习算法', 'FSRCNN深度学习算法', 'AttnSRCNN深度学习算法']:
        zoom_factor = st.number_input('请输入超分辨率的缩放因子, 目前深度学习算法只支持2-4倍', min_value = 2, max_value = 4, step = 1, format='%d')
      else:
        zoom_factor = st.number_input('请输入超分辨率的缩放因子, 目前深度学习算法只支持2-4倍', min_value = 2, max_value = 6, step = 1, format='%d')
      
      if st.button('生成图像'):
        with st.spinner("生成中，请稍等。"):
          im_result  = resize_im(im,zoom_factor,option)
          st.image(im_result, channels="BGR",width=600)
          st.write(im_result.shape)
          img222 = cv2.cvtColor(im_result,cv2.COLOR_BGR2RGB)

          # 持久化到硬盘
          cv2.imwrite("tmp.png", im_result)
        st.success("生成成功，请下载。")
        with open('tmp.png', 'rb') as file:
          btn = st.download_button(
              label="下载图像",
              data=file,
              file_name=f"{file_name.split()[0]}",
              mime="image/png"
            )
        st.subheader("超分效果对比")
        image_comparison(
            img1=cv2.cvtColor(img_result,cv2.COLOR_BGR2RGB),
            img2=cv2.cvtColor(im_result,cv2.COLOR_BGR2RGB),
            label1="原图",
            label2="超分图",
        )
        os.remove("tmp.png")
    else:
      st.error('请上传图像文件', icon="🚨")


# cd E:\系统默认\桌面\挑战者杯\竞赛材料\图像视频超分辨率代码
# streamlit run E:\系统默认\桌面\挑战者杯\竞赛材料\图像视频超分辨率代码\0📸_图像超分辨率.py


