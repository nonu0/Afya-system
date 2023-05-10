# Afya-system
# Django Hospital Management System

This is a Django-based hospital management system that allows users to manage doctors, patients, appointments, and more. It includes various views and models to handle different functionalities of the system.

## Features

- Doctors View: Displays a list of doctors registered in the system.
- Doctor Detail View: Shows detailed information about a specific doctor.
- Home View: Displays the home page with additional information for authenticated users.
- Patient Profile View: Shows the profile page of a patient with their appointment details.
- Show Appointment View: Displays the appointment page for a specific doctor and patient.
- Booked View: Handles the booking of appointments for patients.
- About View: Provides information about the hospital and its mission.
- Department View: Shows the department page with relevant information.
- News View: Displays news articles related to the hospital.
- News Detail View: Shows detailed information about a specific news article.

## Dependencies

This project requires the following dependencies:

- Django (version 4.2.0): A high-level Python web framework.
- Python (version 3.1.1): The programming language used for development.
- Other dependencies: Make sure to install all the required packages mentioned in the `requirements.txt` file.

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```
cd project-directory
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

6. Open your web browser and visit `http://localhost:8000` to access the hospital management system.

## Configuration

- Database: By default, this project uses the SQLite database. If you want to use a different database, update the database settings in the `settings.py` file.

- Static files: The project includes static files such as CSS, JavaScript, and images. Make sure to configure the static file settings in the `settings.py` file to serve these files correctly.

## Usage

- Visit the doctors view to see a list of all registered doctors.
- Click on a doctor to view their detailed information.
- Explore the home page to get an overview of the hospital and additional information for authenticated users.
- Access the patient profile page to view appointment details.
- View the appointment page to schedule an appointment with a specific doctor.
- Book an appointment by selecting the doctor, providing the reason, and choosing the due date.
- Learn about the hospital and its mission on the about page.
- Get information about different departments in the hospital on the department page.
- Read news articles related to the hospital on the news page.
- Click on a news article to view its detailed information.

## Contribution

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as per the license terms.
