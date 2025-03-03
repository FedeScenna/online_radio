from flask import Flask, render_template, Response
from datetime import datetime
import json

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

def render_with_year(template_name, **kwargs):
    kwargs['year'] = datetime.now().year
    return render_template(template_name, **kwargs)

def handler(event, context):
    """Netlify Function handler."""
    path = event.get('path', '').rstrip('/')
    
    if path == '' or path == '/':
        body = render_with_year('index.html', shows=SHOWS)
    elif path == '/schedule':
        body = render_with_year('schedule.html', shows=SHOWS)
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Not Found'})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': body
    } 