from flask import render_template, request, Blueprint
from flask_login import login_required
from orders_manager.models import Post

main = Blueprint('main', __name__)


@main.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    #posts = Post.query.paginate(page=page, per_page=5)
    #posts = Post.query.filter_by(date='15/04/2021').paginate(page=page, per_page=5)
    posts = Post.query.order_by(Post.date.asc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
