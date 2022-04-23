from flask import Flask
import git

app = Flask(__name__)
app.secret_key = "randomstring83209480299-0234"

@app.route('/git_update',methods=['POST'])
def git_update():
    repo = git.Repo('./Todo_App')
    origin = repo.remotes.origin
    repo.create_head('main',
    origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200