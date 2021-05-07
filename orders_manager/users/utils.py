import os
import secrets
from datetime import datetime, timedelta
from PIL import Image
from flask import current_app


def save_picture(form_picture):
    # renaming picture first
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resizing picture before saving
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def change_date_format(date):
    str_date = str(date)
    dt = datetime.strptime(str_date, '%Y-%m-%d').strftime('%d-%m-%Y')
    return dt


def next_day(date):  # function takes a datetime object
    date = date + timedelta(days=1)
    return date.strftime('%d-%m-%Y')


def prev_day(date):  # function takes a datetime object
    date = date - timedelta(days=1)
    return date.strftime('%d-%m-%Y')
