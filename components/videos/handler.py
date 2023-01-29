from werkzeug.utils import secure_filename
from setting import Config
import os
import ffmpeg
from moviepy.editor import VideoFileClip


def temporary_video_loading(raw) -> str:
    new_video_filename = "video_" + \
        str(hash(secure_filename(raw.filename))) + ".mp4"
    video_filepath = os.path.join(
        Config.PATH_TO_DIR+'/static/uploads/v_temp/',
        new_video_filename
    )
    raw.save(video_filepath)
    return video_filepath


def video_open(filepath):
    filename = filepath.split('/')[-1]
    filename = filename.split('.')[0]
    print("Loaded: "+filename)

    video = VideoFileClip(filepath)
    path_to_file = os.path.join(
        Config.PATH_TO_DIR+'/static/uploads/us_videos/', filename+'.webm')
    video.write_videofile(path_to_file)

    print('Complete')
    os.remove(filepath)
    return path_to_file


def dump_video(file):
    meta = ffmpeg.probe(file)
    print(meta['streams'])
    # нужно сделать запрос к БД, который добавит видео в базу
    # прежде всего нужно создать таблицу
