from app import app
from flask import render_template
from app.forms import UserInfoForm, PostForm
from app.models import User, Post
from app import db


@app.route('/')
def index():
    name = 'Dominick'
    title = 'Coding Temple Flask'
    return render_template('index.html', name_of_user=name, title=title)


@app.route('/products')
def test():
    title = 'Coding Temple Products'
    products = ['apple', 'orange', 'banana', 'peach']
    return render_template('products.html', title=title, products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        print('This form has been submitted correctly')
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=register_form)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, user_id=1)
        db.session.add(new_post)
        db.session.commit()
    return render_template('createpost.html', form=form)


    