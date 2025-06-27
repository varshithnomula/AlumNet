# AlumNet - Alumni Networking Platform

## Project Overview
AlumNet is a Django-based web application designed to connect alumni with current students for mentorship, networking, and career guidance. The platform facilitates meaningful connections between graduates and students, helping to build a supportive community that benefits both parties.

## Features

### For Alumni
- **Profile Management**: Create and maintain detailed professional profiles
- **Mentorship Opportunities**: Offer mentorship to current students
- **Networking**: Connect with other alumni and students
- **Contribution Options**: Participate in career talks, share job opportunities, and more

### For Students
- **Alumni Directory**: Browse and search for alumni based on industry, job title, etc.
- **Mentorship Requests**: Send mentorship requests to alumni
- **Career Guidance**: Get advice from professionals in your field of interest
- **Networking**: Build professional connections before graduation

### General Features
- **User Authentication**: Secure login and registration system
- **Dashboard**: Personalized dashboards for both alumni and students
- **Mentorship Management**: Track and manage mentorship requests and relationships

## Technology Stack

- **Backend**: Django 5.1.2
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap 5.3
- **Image Handling**: Pillow 10.4.0

## Installation and Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/alumnet.git
   cd alumnet
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

- **core/**: Main application with models, views, and templates
  - **models.py**: Defines Alumni, Student, and MentorshipRequest models
  - **views.py**: Contains view functions for all pages
  - **templates/**: HTML templates for the frontend
  - **forms.py**: Form definitions for user input
  - **urls.py**: URL routing for the application

## Usage

### For Alumni
1. Register as an alumni with your professional details
2. Complete your profile with mentorship preferences
3. Respond to mentorship requests from students
4. Update your profile as your career progresses

### For Students
1. Register as a student with your academic details
2. Browse alumni profiles to find potential mentors
3. Send mentorship requests with specific goals
4. Manage your mentorship relationships through your dashboard

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django framework and community
- Bootstrap for responsive design
- All contributors and testers