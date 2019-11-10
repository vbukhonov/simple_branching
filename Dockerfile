FROM python:3.7.5-alpine3.10

# Set work directory
WORKDIR /usr/src/simple_branching

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/simple_branching/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/simple_branching/entrypoint.sh

# Copy project
COPY . /usr/src/simple_branching/

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/simple_branching/entrypoint.sh"]