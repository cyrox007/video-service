from sheduler import celery
import sys

if __name__ == "__main__":
    argv = ["worker"]
    celery.start(argv=argv)