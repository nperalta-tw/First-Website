FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME Docker Pro
ENV FLASK_APP=website.py
CMD ["python", "website.py"]