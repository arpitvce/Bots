FROM python:3.10-slim
RUN apt-get update && apt-get install -y \
	chromium\
	chromium-driver\
	wget \
	unzip \
	curl \
	&& rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","endpoint:app","--host","0.0.0.0","--port","8000"]


