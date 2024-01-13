import os
from openxlab.model import download

def Download():
    download(model_repo='OpenLMLab/InternLM-chat-7b',output='/home/xlab-app-center/InternLM-chat-7b')
    download(model_repo='EnableAsync/openxlab-assistant',output="/home/xlab-app-center/hf")

Download()
os.system('echo $PWD')
os.system('ls')

os.system('xtuner convert merge /home/xlab-app-center/InternLM-chat-7b /home/xlab-app-center/hf /home/xlab-app-center/hf-merge --max-shard-size 2GB')
os.system('streamlit run /home/xlab-app-center/InternLM/web_demo.py --server.address=0.0.0.0 --server.port 7860')