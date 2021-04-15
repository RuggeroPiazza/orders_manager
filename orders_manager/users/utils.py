import os
import secrets
from datetime import datetime
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
    dt = datetime.strptime(str_date, '%Y-%m-%d').strftime('%d/%m/%Y')
    return dt


days_per_month = {1: 31,  # {month : num of days, ... }
                  2: 30,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}


def next_day(day, month, year):
    if day < days_per_month[month]:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1

    str_date = str(day) + '/' + str(month) + '/' + str(year)
    return str_date


def prev_day(day, month, year):
    if day > 1:
        day -= 1
    else:
        if month > 1:
            month -= 1
            day = days_per_month[month]
        else:
            day = 31
            month = 12
            year -= 1

    str_date = str(day) + '/' + str(month) + '/' + str(year)
    return str_date
