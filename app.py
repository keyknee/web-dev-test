from flask import Flask, render_template, url_for
from data import logic

app = Flask(__name__)
 
def item_pages():
    for item in logic.items:
        new_route = item.title

@app.route('/')
def home():

    return render_template('home.html',
        users=logic.users,
        items=logic.items,
        active_user = logic.active_user,
        createUser = logic.User,
        setActiveUser=logic.User.setActiveUser
    )

@app.route('/<item_name>')
def item(item_name):
    return render_template('item.html'
    )

if __name__ == '__main__':
    app.run(debug=True)