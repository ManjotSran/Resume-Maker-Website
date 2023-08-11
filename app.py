from flask import Flask, render_template, request, send_file, redirect, url_for
import pdfkit

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/build', methods=['GET', 'POST'])
def build_resume():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        education = request.form.get('education')
        experience = request.form.get('experience')
        certifications = request.form.get('certifications')
        skills = request.form.get('skills')
        projects = request.form.get('projects')
        languages = request.form.get('languages')

        # Read the CSS content
        with open("static/styles.css", "r") as css_file:
            css_content = css_file.read()

        # Generate a resume in PDF format using the input
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
    {css_content}
    </style>
</head>
<body>
    <h1>{name}</h1>
    <h2>Contact Information</h2>
    <p><strong>Address:</strong> {address}</p>
    <h2>Education</h2>
    <p>{education}</p>
    <h2>Experience</h2>
    <p>{experience}</p>
    <h2>Certifications</h2>
    <p>{certifications}</p>
    <h2>Skills</h2>
    <p>{skills}</p>
    <h2>Projects</h2>
    <p>{projects}</p>
    <h2>Languages</h2>
    <p>{languages}</p>
    <div class="footer">Generated using ResumeBuilder</div>
</body>
</html>
"""

        pdf = pdfkit.from_string(html_content, False)
        with open("resume.pdf", "wb") as f:
            f.write(pdf)

        return send_file("resume.pdf", as_attachment=True, download_name=f"{name}_resume.pdf")

    return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







