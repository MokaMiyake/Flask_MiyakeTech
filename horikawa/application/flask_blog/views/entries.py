from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_blog import db
from flask_blog.views.views import login_required

@app.route("/")
@login_required
def show_entries():
    # "@login_required"で下記2行のコードをviews/views.py内のlogin_required関数で実行
    # if not session.get("logged_in"):
    #     return redirect(url_for("login"))
    
    print("session.get('logged_in'):" + str(session.get("logged_in")))

    entries = Entry.query.order_by(Entry.id.desc()).all()

    return render_template("entries/index.html",entries=entries)


@app.route("/entries", methods=["POST"])
@login_required
def add_entry():
    entry = Entry(
        title = request.form["title"],
        text = request.form["text"]
    )

    db.session.add(entry)
    db.session.commit()
    flash("新しく記事が作成されました")

    return redirect(url_for("show_entries"))


@app.route("/entries/new", methods=["GET"])
@login_required
def new_entry():
    return render_template("entries/new.html")


@app.route("/entries/<int:id>", methods=["GET"])
@login_required
def show_entry(id):
    entry = Entry.query.get(id)
    return render_template("entries/show.html", entry=entry)

@app.route("/entris/<int:id>/edit", methods=["GET"])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template("entries/edit.html", entry=entry)


@app.route("/entris/<int:id>/update", methods=["POST"])
@login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form["title"]
    entry.text = request.form["text"]

    db.session.merge(entry)
    db.session.commit()

    flash("記事が更新されました")
    return redirect(url_for("show_entries"))


@app.route("/entris/<int:id>/delete", methods=["POST"])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()

    flash("投稿が削除されました")
    return redirect(url_for("show_entries"))