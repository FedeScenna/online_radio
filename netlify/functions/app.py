from flask import Flask, render_template
from datetime import datetime
import serverless_wsgi

app = Flask(__name__)

# Add current year to all templates
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

# Sample show data - in a real application, this would come from a database
SHOWS = [
    {
        'title': 'Morning Jazz',
        'description': 'Start your day with smooth jazz tunes',
        'soundcloud_url': 'https://soundcloud.com/fedescn/slowed-signs',
        'time': '08:00 - 10:00',
        'days': 'Monday - Friday'
    },
    {
        'title': 'Electronic Beats',
        'description': 'The best in electronic music',
        'soundcloud_url': 'https://soundcloud.com/fedescn/slowed-signs',
        'time': '20:00 - 22:00',
        'days': 'Saturday'
    }
]

@app.route('/')
def index():
    return render_template('index.html', shows=SHOWS)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', shows=SHOWS)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context) 