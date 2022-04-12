from flask import Flask, render_template, request, url_for
from data import logic

app = Flask(__name__)
app.config['SECRET_KEY'] = '2e85f9a9123bfd19a26869d910e61277be99f119f09f6c81'


@app.route('/')
def home():

    return render_template('home.html',
        users=logic.users,
        items=logic.items,
        active_user = logic.active_user,
        createUser = logic.User,
        setActiveUser=logic.User.setActiveUser
    )


if __name__ == '__main__':
    app.run(debug=True)