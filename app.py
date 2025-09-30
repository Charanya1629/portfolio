# app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# IMPORTANT: Set a secret key for flash messages and session security
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# 1. Index Route: The main portfolio page
@app.route('/')
def index():
    # Data to pass to the template (optional, but good practice)
    user_data = {
        'name': 'GANGAM CHARANYA REDDY',
        'skills': [
            'Python', 'C', 'HTML', 'MySQL', 
            'AWS Academy Graduate - Cloud Foundations [cite: 76]', 
            'Data Analytics (Certified) [cite: 77]',
            'Machine Learning with python [cite: 75]'
        ],
        'project_title': 'AI BASED SMART HOME ENERGY MANAGEMENT [cite: 66]'
    }
    # Renders the index.html template and passes data
    return render_template('index.html', data=user_data)

# 2. Contact Route: Handles the contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # If the request method is POST, the user submitted the form
    if request.method == 'POST':
        # Get data from the form fields
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # NOTE: In a real-world app, you would send this data to an email service or database here.
        
        # Flash a success message
        flash(f'Thank you, {name}! Your message has been received.', 'success')
        
        # Redirect the user back to the index page after successful submission
        return redirect(url_for('index'))
        
    # If the request method is GET, just display the contact section (or a dedicated page)
    # We will embed the form on the index.html, so this route redirects back there.
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)

