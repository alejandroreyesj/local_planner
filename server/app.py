from flask import Flask, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/calendar/current-month', methods=['GET'])
def get_current_month():
    today = datetime.now()
    first_day = today.replace(day=1)
    last_day = (first_day + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    return jsonify({
        'current_month': {
            'name': today.strftime('%B'),
            'year': today.year,
            'days_in_month': last_day.day,
            'first_day_of_week': first_day.weekday(),
            'today': today.day
        }
    })

if __name__ == '__main__':
    app.run(debug=True) 