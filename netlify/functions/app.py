from datetime import datetime
import json
from pathlib import Path
import os

# Sample show data
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

def read_template(template_name):
    template_path = Path(__file__).parent / 'templates' / template_name
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def handler(event, context):
    """Netlify Function handler."""
    path = event.get('path', '').rstrip('/')
    
    try:
        if path == '' or path == '/':
            template = read_template('index.html')
        elif path == '/schedule':
            template = read_template('schedule.html')
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Not Found'})
            }

        # Simple template variable replacement
        current_year = datetime.now().year
        content = template.replace('{{ year }}', str(current_year))
        
        # Replace show data
        if '{% for show in shows %}' in content:
            show_html = ''
            for show in SHOWS:
                show_template = '''
                <div class="card">
                    <h3>{title}</h3>
                    <p>{description}</p>
                    <p><strong>Time:</strong> {time}</p>
                    <p><strong>Days:</strong> {days}</p>
                    <div class="soundcloud-player">
                        <iframe
                            width="100%"
                            height="166"
                            scrolling="no"
                            frameborder="no"
                            allow="autoplay"
                            src="https://w.soundcloud.com/player/?url={url}&color=%231DB954&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false"
                        ></iframe>
                    </div>
                </div>
                '''.format(
                    title=show['title'],
                    description=show['description'],
                    time=show['time'],
                    days=show['days'],
                    url=show['soundcloud_url']
                )
                show_html += show_template
            
            start = content.find('{% for show in shows %}')
            end = content.find('{% endfor %}') + len('{% endfor %}')
            content = content[:start] + show_html + content[end:]

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': content
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        } 