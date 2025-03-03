from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__, 
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))

# Add current year to all templates
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

# Sample show data with episodes
SHOWS = {
    'morning_jazz': {
        'title': 'Morning Jazz',
        'schedule': 'Weekdays 8:00 AM - 10:00 AM',
        'description': 'Start your day with smooth jazz selections from classic and contemporary artists. A perfect blend of instrumental and vocal jazz to energize your morning.',
        'episodes': [
            {
                'date': 'March 15, 2024',
                'title': 'Morning Jazz - Smooth Awakening',
                'soundcloud_url': 'https://soundcloud.com/your-morning-jazz/smooth-awakening'
            },
            {
                'date': 'March 14, 2024',
                'title': 'Morning Jazz - Classic Standards',
                'soundcloud_url': 'https://soundcloud.com/your-morning-jazz/classic-standards'
            }
        ]
    },
    'electronic_beats': {
        'title': 'Electronic Beats',
        'schedule': 'Weekends 9:00 PM - 11:00 PM',
        'description': 'Immerse yourself in the world of electronic music, featuring the best in house, techno, and ambient. From underground gems to electronic classics.',
        'episodes': [
            {
                'date': 'March 16, 2024',
                'title': 'Electronic Beats - Deep House Journey',
                'soundcloud_url': 'https://soundcloud.com/your-electronic-beats/deep-house-journey'
            },
            {
                'date': 'March 9, 2024',
                'title': 'Electronic Beats - Techno Night',
                'soundcloud_url': 'https://soundcloud.com/your-electronic-beats/techno-night'
            }
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shows')
def shows():
    return render_template('shows.html')

@app.route('/shows/morning-jazz')
def morning_jazz():
    return render_template('show_detail.html', show=SHOWS['morning_jazz'])

@app.route('/shows/electronic-beats')
def electronic_beats():
    return render_template('show_detail.html', show=SHOWS['electronic_beats'])

# For Netlify deployment
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True) 