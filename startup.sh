# startup.sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

chmod +x startup.sh
    