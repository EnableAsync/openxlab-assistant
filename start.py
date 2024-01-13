import os
from openxlab.model import download

def Download():
    download(model_repo='OpenLMLab/InternLM-chat-7b',output='/home/xlab-app-center/InternLM-chat-7b')

Download()

os.system('xtuner convert merge /home/xlab-app-center/InternLM-chat-7b ./hf ./hf-merge --max-shard-size 2GB')



os.system('streamlit run ./InternLM/app.py --server.address=0.0.0.0 --server.port 7860')