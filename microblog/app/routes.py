from app import app

@app.route('/')
@app.route('/index')

def index():
  return "The traditional greeting for a new programming exercise."
