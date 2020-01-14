from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
# from .forms import 
# from ..models import Review

@main.route("/", methods = ["GET", "POST"])
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    all_posts = Post.query.all()
    post_form = PostForm()
    title = "60 Seconds | Leave a mark"

    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_form.title.data = ""
        post_content = post_form.post.data
        post_form.post.data = ""
        post_category = post_form.category.data
        new_post = Post(post_title = post_title,
                        post_content = post_content,
                        category = post_category,
                        user_id = current_user.id)

        new_post.save_post()
        return redirect(url_for("main.index"))
    
    return render_template("index.html",
                            title = title,
                            post_form = post_form,
                            all_posts = all_posts)