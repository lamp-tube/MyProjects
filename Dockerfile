# Python 3.11 image
FROM python:3.11

# /app as working directory in the application container
WORKDIR /app

# Copying all required files into the container in /app folder
# COPY task.py /app/

# COPY orders.csv /app/

# COPY orders_test-1.csv /app/

# COPY orders_test-2.csv /app/

# COPY requirements.txt /app/

# Installing packages from requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copying entire current directory into the container in /app directory
COPY . /app/

# command to run task.py python script, by default it will run on orders.csv file
CMD ["python", "task.py"]
