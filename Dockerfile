# FROM microsoft/aspnet
FROM python:3.8

# RUN echo 'pull down choco'
# RUN powershell -Command Install-PackageProvider -name chocolatey -Force
# RUN powershell -Command Set-PackageSource -Name chocolatey -Trusted

# RUN powershell -Command Get-PackageSource

# RUN echo 'install chrome via choco'
# RUN powershell -Command Install-Package GoogleChrome -MinimumVersion 74

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -\
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb" stable main >> /etc/apt/sources.list.d/google-chrome.list'\
    && apt-get -y update\
    && apt-get install -y google-chrome-stable

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]