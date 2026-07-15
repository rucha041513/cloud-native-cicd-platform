FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a non-root user
RUN useradd -m flaskuser

# Give permissions
RUN chown -R flaskuser:flaskuser /app

# Switch user
USER flaskuser

EXPOSE 5000

CMD ["python","app.py"]