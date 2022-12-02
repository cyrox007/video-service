from werkzeug.utils import secure_filename
from setting import Config
import os

def upload(file):
    if file.filename == '':
        return 'uploads/us_avatars/user_default.jpg'
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(Config.FULL_AVATAR_DIR, filename))

    return Config.AVATAR_DIR+filename