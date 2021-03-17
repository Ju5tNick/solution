from flask import Flask, render_template 
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    users = db_sess.query(User)
    coll = {user.id: ' '.join([user.name, user.surname]) for user in users}
    return render_template("work_log.html", jobs=jobs, coll=coll)


if __name__ == '__main__':
    main()