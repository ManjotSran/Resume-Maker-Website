# Resume-Maker-Website

# CS50 Final Project: Instant Professional Resume Builder
#### Video Demo: https://youtu.be/L1HQKZFhoxk
#### Description:
The project, conceptualized and developed by Manjot Sran after completing the CS50 course, is a web application built using the Flask framework. It aims to provide a seamless experience for users to generate professional resumes. The application's primary feature is its user-friendly interface where users input their personal and professional details, and within moments, they receive a well-structured, sleek resume ready for job applications or personal branding.

Key Highlights:
- **Simplicity**: With an intuitive design, the application ensures users don't have to grapple with complex settings or configurations.
- **Quick Turnaround**: The app's efficiency ensures that users receive their professional resume within seconds.
- **Tech Stack**: Leveraging the Flask framework, the project exhibits the potential of using Python for web development.

Whether you are a student, job seeker, or someone looking to update their resume, this tool is designed to cater to diverse needs, ensuring everyone gets a resume they are proud to share.

Feedback and suggestions are always welcome. If you find any bugs or wish to see a new feature, feel free to raise an issue or contribute to the project.

The project consists of several key files:

#### app.py:

The backbone of the application, this file sets up the Flask application and contains the necessary routes to render our web pages and handle form submissions.
Contains the logic to generate PDFs using the ReportLab library based on user inputs.
The PDF generation logic includes formatting and styling details to make the resume look professional.

#### home.html:

This is the landing page for the application.
Features a clean and intuitive design, guiding the user to either start building their resume or learn more about the application's offerings.
Uses the Bootstrap framework for responsive design, ensuring the page looks great on all devices.
Also contains a parallax effect for a modern and engaging user experience.

#### index.html:

This is the main form page where users input their details to generate a resume.
It collects information about the user's name, address, education, experience, certifications, skills, projects, and languages.
Once submitted, the provided data is used to generate a personalized resume in PDF format.

#### styles.css:

Contains styling for index.html.
Ensures the form is displayed in a user-friendly and aesthetically pleasing manner.

#### styles1.css:

Contains styling details for home.html.
Includes the necessary CSS to create the parallax effect and ensure all elements on the page are displayed correctly and responsively.
