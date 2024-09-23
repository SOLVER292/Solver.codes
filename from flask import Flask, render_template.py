from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize an empty list to store user information
user_list = []

# Route to handle the login form and store user information
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['fname']
        password = request.form['pass']
        gmail = request.form['gmail']
        
        user_info = {
            'username': username,
            'password': password,
            'gmail': gmail
        }
        user_list.append(user_info)
        print("User information added successfully!")

    return render_template('login.html')

# Route to display the list of users (for demonstration purposes)
@app.route('/users')
def users():
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)
