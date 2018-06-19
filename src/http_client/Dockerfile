FROM python:3.6

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
COPY app /usr/src/app

ENV DISPLAY=:99

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "run.py" "-p" "https://www.seznam.cz"]