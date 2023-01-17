from werkzeug.utils import secure_filename
from setting import Config
import os
import cv2

def image_verification_and_processing(img, filename) -> str:
    loaded_img = cv2.imread(img, cv2.IMREAD_COLOR)
    cropped_image = crop_image(loaded_img)
    changed_size_img = resize(cropped_image)
    new_filename: str = "photo_"+str(hash(filename))+".webp"
    full_path_file = os.path.join(Config.FULL_AVATAR_DIR, new_filename) # путь для сохранения
    path_to_the_file = os.path.join(Config.AVATAR_DIR, new_filename) # путь для БД
    cv2.imwrite(full_path_file, changed_size_img, [cv2.IMWRITE_WEBP_QUALITY]) # Сохраняем
    return path_to_the_file

def resize(img, interp=cv2.INTER_LINEAR):
    new_width = 150 
    new_height = 150
    h, w = img.shape[:2]
    if img.shape[0] > 150 or img.shape[1] > 150:
        if new_width is None and new_height is None:
            return img

        if new_width is None:
            ratio = new_height / h
            dimension = (int(w * ratio), new_height)
            
        else: 
            ratio = new_width / w
            dimension = (new_width, int(h * ratio))
            
        return cv2.resize(img, dimension, interpolation=interp)
    
    return img


def crop_image(img: cv2.imread):
    himg = img.shape[0] # height
    wimg = img.shape[1] # width
    if himg == wimg:
        return img

    if himg > wimg:
        size = int((himg - wimg) / 2)
        begin_coord_y = int(size)
        end_coord_y = int(himg-size)
        return img[begin_coord_y:end_coord_y, 0:wimg]
    else:
        size = int((wimg - himg) / 2)
        begin_coord_x = int(size)
        end_coord_x = int(wimg-size)
        return img[0:himg, begin_coord_x:end_coord_x]

    
def temporary_saving(file) -> str:
    temp_filepath = os.path.join(
        Config.PATH_TO_DIR+'/static/uploads/av_temp/', 
        secure_filename(file.filename)
        )
    file.save(temp_filepath)
    return temp_filepath

def avatar_processing(file) -> str:
    if file.filename == '':
        return 'uploads/us_avatars/user_default.jpg'
    
    filepath = temporary_saving(file=file)
    avatar = image_verification_and_processing(filepath, file.filename.split('.')[0])
    os.remove(filepath)

    return avatar