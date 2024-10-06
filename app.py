from flask import Flask, request, render_template
import requests
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def index():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('index-web.html', today_date=today_date)
@app.route('/demo')
def demo():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('demo.html', today_date=today_date)
@app.route('/contact')
def contact():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('contact.html', today_date=today_date)
@app.route('/space')
def space():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('form.html', today_date=today_date)

@app.route('/login')
def login():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('login.html', today_date=today_date)

@app.route('/about')
def about():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date
    return render_template('about.html', today_date=today_date)

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    today_date = datetime.now().strftime("%Y-%m-%d")  # Get today's date again
    
    if request.method == 'POST':
        # Get the selected API and dates from the form
        api_choice = request.form.get('api_choice')
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        # Initialize the filtered_data variable
        filtered_data = []
        # Determine the URL based on the API choice
        if api_choice == 'solar_flare':
            url = f"https://api.nasa.gov/DONKI/FLR?startDate={start_date_str}&endDate={end_date_str}&api_key=DEMO_KEY"
        elif api_choice == 'cme_analysis':
            url = f"https://api.nasa.gov/DONKI/CMEAnalysis?startDate={start_date_str}&endDate={end_date_str}&mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&api_key=DEMO_KEY"
        elif api_choice == 'geomagnetic_storms':
            url = f"https://api.nasa.gov/DONKI/GST?startDate={start_date_str}&endDate={end_date_str}&api_key=DEMO_KEY"
        elif api_choice == 'solar_energetic_particles':
            url = f"https://api.nasa.gov/DONKI/SEP?startDate={start_date_str}&endDate={end_date_str}&api_key=DEMO_KEY"
        elif api_choice == 'magnetosphere':
            url = f"https://api.nasa.gov/DONKI/MPC?startDate={start_date_str}&endDate={end_date_str}&api_key=DEMO_KEY"
        elif api_choice == 'high_speed_streams':
            url = f"https://api.nasa.gov/DONKI/HSS?startDate={start_date_str}&endDate={end_date_str}&api_key=DEMO_KEY"
        elif api_choice == 'interplanetary_shock':
            url = f"https://api.nasa.gov/DONKI/IPS?startDate={start_date_str}&endDate={end_date_str}&location=Earth&catalog=ALL&api_key=DEMO_KEY"
        elif api_choice == 'notification':
            url = f"https://api.nasa.gov/DONKI/notifications?startDate=2014-05-01&endDate=2014-05-08&type=all&api_key=DEMO_KEY"
        elif api_choice == 'picture':
            url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        elif api_choice == 'fhac':
            url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY"
        elif api_choice == 'rhac':
            url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=rhaz&api_key=DEMO_KEY"
        elif api_choice == 'nc':
            url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=navcam&api_key=DEMO_KEY"
        elif api_choice == 'eimg':
            url = f"https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY"
        elif api_choice == 'obimg':
            url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY"
        else:
            return "Invalid API choice", 400
        # Make the API request
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the response
            filtered_data = data  # Store the data to be rendered
        else:
            filtered_data = []
        # Render the appropriate template based on the API choice
        if api_choice == 'solar_flare':
            return render_template('SolarFlare.html', filtered_data=filtered_data)
        elif api_choice == 'cme_analysis':
            return render_template('cmeanalysis.html', filtered_data=filtered_data)
        elif api_choice == 'geomagnetic_storms':
            return render_template('geomagnetic.html', filtered_data=filtered_data)
        elif api_choice == 'solar_energetic_particles':
            return render_template('solarener.html', filtered_data=filtered_data)
        elif api_choice == 'magnetosphere':
            return render_template('magneto.html', filtered_data=filtered_data)
        elif api_choice == 'high_speed_streams':
            return render_template('highspeed.html', filtered_data=filtered_data)
        elif api_choice == 'interplanetary_shock':
            return render_template('interplane.html', filtered_data=filtered_data)
        elif api_choice == 'notification':
            return render_template('notification.html', filtered_data=filtered_data)
        elif api_choice == 'picture':
            return render_template('picture.html', filtered_data=filtered_data)
        elif api_choice == 'fhac':
            return render_template('fhac.html', filtered_data=filtered_data)
        elif api_choice == 'rhac':
            return render_template('rhac.html', filtered_data=filtered_data)
        elif api_choice == 'nc':
            return render_template('nc.html', filtered_data=filtered_data)
        elif api_choice == 'eimg':
            return render_template('eimg.html', filtered_data=filtered_data)
        elif api_choice == 'obimg':
            return render_template('obimg.html', filtered_data=filtered_data)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)