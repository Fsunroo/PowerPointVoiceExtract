FROM python:3.7
COPY . .
RUN apt-get update && apt-get install -y python3-pip && pip3 install -r requirements.txt
RUN apt-get install ffmpeg -y
CMD ["python", "bot.py"]