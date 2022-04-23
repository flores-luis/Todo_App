from flask_app import app
#had an issue here importing because of an empty space causing import issues
#now resolved
from flask_app.controllers import tasks 


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)

