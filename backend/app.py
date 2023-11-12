from flask import Flask, session, request, redirect, url_for
import retrieveagent 

app = Flask(__name__)

@app.route('/set_name', methods=['POST'])
def set_name():
    new_name = request.form['new_name']
    session['user_name'] = new_name
    return redirect(url_for('get_name'))

@app.route('/get_name')
def get_name():
    user_name = session.get('user_name')
    return f'User Name: {user_name}'

@app.route('/initialize_agents')
def get_name():
    user_name = session.get('user_name')
    return f'User Name: {user_name}'


if __name__ == '__main__':
    app.run(debug=True)