from flask import request, redirect, url_for, render_template, flash, session
from message import app
from message import db
from message.models.entries import Chat
from message.views.views import login_required

@app.route("/")
def login_get():
    if 'login' not in session:
        session['login'] = 'logged_out'
    return render_template("login.html")

@app.route("/login_in")
def login_in():
    session['login'] = "login_in"
    return redirect(url_for('login_get'))

@app.route("/login_new")
def login_new():
    session['login'] = "login_new"
    return redirect(url_for('login_get'))


# @app.route('/entries/new', methods=['GET'])
# @login_required
# def new_entry():
#     return render_template('entries/new.html')

# @app.route('/entries', methods=['POST'])
# @login_required
# def add_entry():
#     entry = Entry(
#         title=request.form['title'],
#         text=request.form['text']
#     )
#     db.session.add(entry)
#     db.session.commit()
#     flash('新しく記事が作成されました')
#     return redirect(url_for('show_entries'))


# @app.route('/entries/<int:id>/edit', methods=['GET'])
# @login_required
# def edit_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/edit.html', entry=entry)


# @app.route('/entries/<int:id>', methods=['GET'])
# @login_required
# def show_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/show.html', entry=entry)



# @app.route('/entries/<int:id>/update', methods=['POST'])
# @login_required
# def update_entry(id):
#     entry = Entry.query.get(id)
#     entry.title = request.form['title']
#     entry.text = request.form['text']
#     db.session.merge(entry)
#     db.session.commit()
#     flash('記事が更新されました')
#     return redirect(url_for('show_entries'))



# @app.route('/entries/<int:id>/delete', methods=['POST'])
# @login_required
# def delete_entry(id):
#     entry = Entry.query.get(id)
#     db.session.delete(entry)
#     db.session.commit()
#     flash('投稿が削除されました')
#     return redirect(url_for('show_entries'))