import os

try:
    port = int(os.environ.get('PORT', 8000))
except (ValueError, TypeError):
    port = 8000

bind = f"0.0.0.0:{port}"
timeout = 120
workers = 1

log_level = "INFO"


def when_ready(server):
    server.log.info(f"Started the service...")
