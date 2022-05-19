FROM python:3.8
LABEL build_type="yinsh"

COPY requirements.txt /

RUN pip install --upgrade \ 
pip install -r requirements.txt 

WORKDIR "/code"
