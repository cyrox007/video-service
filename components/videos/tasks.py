from run_celery import celery
from components.videos.handler import video_open, dump_video


@celery.task
def video_processing(path_to_file):
    file = video_open(path_to_file)
    dump_video(file)