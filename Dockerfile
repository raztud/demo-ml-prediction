FROM python:3.11-slim-bookworm

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# hadolint ignore=DL3008
RUN apt-get update  \
    && apt-get install -y --no-install-recommends curl gcc build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV HOME=/app \
    PYTHONPATH=/app

RUN mkdir -p $HOME $HOME/model
WORKDIR $HOME

COPY ./src/ $HOME/src/
COPY ./gunicorn.conf.py ./requirements.txt $HOME/

RUN pip install --no-cache-dir -r $HOME/requirements.txt

ENTRYPOINT [ "gunicorn" ]
CMD ["--config", "/app/gunicorn.conf.py", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]
