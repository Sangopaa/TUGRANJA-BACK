FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:5001", "app:create_flask_app()"]