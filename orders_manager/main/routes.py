from flask import render_template, request, Blueprint, redirect
from flask_login import login_required
from orders_manager.models import Post
from orders_manager.users.utils import next_day, prev_day
from datetime import datetime, date

main = Blueprint('main', __name__)

main_date = date.today()

@main.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    global main_date
    main_date = date.today()
    today = main_date.strftime("%d/%m/%Y")
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(date=today).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, date=today)


@main.route("/timeline/<string:when>", methods=['GET', 'POST'])
@login_required
def timeline(when):
    global main_date
    if when == 'next':
        new_date = next_day(main_date)
        main_date = datetime.strptime(new_date, '%d/%m/%Y')

    if when == 'prev':
        new_date = prev_day(main_date)
        main_date = datetime.strptime(new_date, '%d/%m/%Y')

    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(date=new_date).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, date=new_date)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
