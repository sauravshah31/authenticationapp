
FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
EXPOSE 8000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
