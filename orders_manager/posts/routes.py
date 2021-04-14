from flask import render_template, redirect, request, abort, url_for, flash, Blueprint
from flask_login import current_user, login_required
from orders_manager import db
from orders_manager.models import Post
from orders_manager.posts.forms import PostForm
from orders_manager.users.utils import change_date_format


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_date_format = change_date_format(form.date.data)
        post = Post(name=form.name.data,
                    phone_number=form.phone_number.data,
                    date=new_date_format,
                    order=form.order.data,
                    post_code=form.post_code.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your order has been created!", 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Order', form=form, legend='New Order')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.name, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.name = form.name.data
        post.phone_number = form.phone_number.data
        #post.date = form.date.data
        post.order = form.order.data
        post.post_code = form.post_code.data
        db.session.commit()
        flash("Your order has been updated!", 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.name.data = post.name
        form.phone_number.data = post.phone_number
        #form.date.data = post.date
        form.order.data = post.order
        form.post_code.data = post.post_code
    return render_template('create_post.html', title='Update Order', form=form, legend='Update Order')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your order has been deleted", 'success')
    return redirect(url_for('main.home'))
