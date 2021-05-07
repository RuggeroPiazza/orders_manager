from flask import render_template, request, Blueprint, redirect, session, url_for
from flask_login import login_required
from orders_manager.models import Post
from orders_manager.users.utils import next_day, prev_day
from datetime import datetime, date

main = Blueprint('main', __name__)


@main.route("/home/", defaults={'view_date': date.today().strftime("%d-%m-%Y")})
@main.route("/home/<string:view_date>", methods=['GET', 'POST'])
@login_required
def home(view_date):
    session['date'] = view_date
    today = session.get('date')
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(date=today).paginate(page=page, per_page=5)

    return render_template('home.html', posts=posts, date=today)


@main.route("/redirect_home/<string:when>", methods=['GET', 'POST'])
@login_required
def redirect_home(when):
    session_date = session.get('date')
    main_date = datetime.strptime(session_date, '%d-%m-%Y')
    if when == 'next':
        new_date = next_day(main_date)
        session['date'] = new_date
    if when == 'prev':
        new_date = prev_day(main_date)
        session['date'] = new_date

    return redirect(url_for('main.home', view_date=new_date))


@main.route("/about")
def about():
    return render_template('about.html', title='About')
