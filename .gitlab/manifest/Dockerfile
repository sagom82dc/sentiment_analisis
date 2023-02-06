FROM python:3.7-stretch  as builder
LABEL "maintaner"="Alessandra Botto"

ENV VENV="/venv"
ENV PATH="${VENV}/bin:${PATH}"
ARG USER
ARG PASSWORD

COPY requirements.txt .
RUN python -m venv ${VENV} && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
FROM python:3.7-stretch

# setup venv with dependencies from the builder stage
ENV VENV="/venv"
ENV PATH="${VENV}/bin:$PATH"
COPY --from=builder ${VENV} ${VENV}

# copy app files
RUN mkdir sentiment_analisis
WORKDIR /sentiment_analisis
COPY . .

EXPOSE 5050
RUN export PYTHONPATH=${PWD}
CMD [ "python", "-m", "wsgi" ]