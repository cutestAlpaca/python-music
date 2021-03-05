FROM python:3.7-slim

ENV WORKDIR /var/www/main
RUN /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install flask Beautifulsoup4 requests -i https://mirrors.aliyun.com/pypi/simple/
COPY ./ $WORKDIR/main
EXPOSE 6688
#CMD ["python ./OpenMusic/app.py"]
WORKDIR $WORKDIR
CMD python3 $WORKDIR/main/app.py