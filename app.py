from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import os
import json
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages and session

# Add current year to all templates
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

# Load shows data from JSON file or create default if not exists
def load_shows():
    try:
        with open('data/shows.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Create default shows data
        default_shows = {
            'morning_jazz': {
                'title': 'Spectral Mornings',
                'schedule': 'Weekdays 8:00 AM - 10:00 AM',
                'description': 'Start your day with smooth jazz selections from classic and contemporary artists. A perfect blend of instrumental and vocal jazz to energize your morning.',
                'episodes': [
                    {
                        'id': str(uuid.uuid4()),
                        'date': 'March 15, 2024',
                        'title': 'Spectral Mornings - Smooth Awakening',
                        'platform': 'mixcloud',
                        'mixcloud_url': 'https://www.mixcloud.com/austral-waves/spectral-mornings-smooth-awakening/'
                    },
                    {
                        'id': str(uuid.uuid4()),
                        'date': 'March 14, 2024',
                        'title': 'Spectral Mornings - Classic Standards',
                        'platform': 'soundcloud',
                        'soundcloud_url': 'https://soundcloud.com/your-morning-jazz/classic-standards'
                    }
                ]
            },
            'electronic_beats': {
                'title': 'Rythms Disjunctions',
                'schedule': 'Weekends 9:00 PM - 11:00 PM',
                'description': 'Immerse yourself in the world of electronic music, featuring the best in house, techno, and ambient. From underground gems to electronic classics.',
                'episodes': [
                    {
                        'id': str(uuid.uuid4()),
                        'date': 'March 16, 2024',
                        'title': 'Rythms Disjunctions - Deep House Journey',
                        'platform': 'mixcloud',
                        'mixcloud_url': 'https://www.mixcloud.com/austral-waves/rythms-disjunctions-deep-house-journey/'
                    },
                    {
                        'id': str(uuid.uuid4()),
                        'date': 'March 9, 2024',
                        'title': 'Rythms Disjunctions - Techno Night',
                        'platform': 'soundcloud',
                        'soundcloud_url': 'https://soundcloud.com/your-electronic-beats/techno-night'
                    }
                ]
            }
        }
        
        # Ensure data directory exists
        os.makedirs('data', exist_ok=True)
        
        # Save default shows
        with open('data/shows.json', 'w') as f:
            json.dump(default_shows, f, indent=4)
            
        return default_shows

# Save shows data to JSON file
def save_shows(shows):
    with open('data/shows.json', 'w') as f:
        json.dump(shows, f, indent=4)

# Global shows data
SHOWS = load_shows()

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

@app.route('/admin')
def admin():
    return render_template('admin.html', shows=SHOWS)

@app.route('/admin/add-episode', methods=['GET', 'POST'])
def add_episode():
    if request.method == 'POST':
        show_id = request.form.get('show_id')
        title = request.form.get('title')
        date = request.form.get('date')
        platform = request.form.get('platform')
        url = request.form.get('url')
        
        if not all([show_id, title, date, platform, url]):
            flash('All fields are required', 'error')
            return redirect(url_for('add_episode'))
            
        if show_id not in SHOWS:
            flash('Invalid show selected', 'error')
            return redirect(url_for('add_episode'))
            
        # Create new episode
        new_episode = {
            'id': str(uuid.uuid4()),
            'date': date,
            'title': title,
            'platform': platform
        }
        
        # Add platform-specific URL
        if platform == 'mixcloud':
            new_episode['mixcloud_url'] = url
        elif platform == 'soundcloud':
            new_episode['soundcloud_url'] = url
            
        # Add to show episodes
        SHOWS[show_id]['episodes'].insert(0, new_episode)  # Add to beginning of list
        
        # Save updated shows data
        save_shows(SHOWS)
        
        flash('Episode added successfully', 'success')
        return redirect(url_for('admin'))
        
    return render_template('add_episode.html', shows=SHOWS)

@app.route('/admin/delete-episode/<show_id>/<episode_id>', methods=['POST'])
def delete_episode(show_id, episode_id):
    if show_id in SHOWS:
        SHOWS[show_id]['episodes'] = [ep for ep in SHOWS[show_id]['episodes'] if ep['id'] != episode_id]
        save_shows(SHOWS)
        flash('Episode deleted successfully', 'success')
    else:
        flash('Show not found', 'error')
        
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True) 