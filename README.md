# AgeWELL-Hackathon
 
WebApp to help the elderly

# Flask Authentication Application

This repository contains a simple Flask web application that handles user authentication with SQLite as the backend database. 

## Features

- **Login Page**: Users can log in with their credentials.
- **Registration Page**: New users can register an account.
- **Authentication**: The app authenticates users based on their username and password stored in the SQLite database.
- **Redirects**: 
  - Successful login redirects to a home page.
  - Failed login redirects to the registration page.
  - Successful registration redirects back to the login page.

## File Structure

- `app.py`: The main Flask application file containing routes and logic.
- `templates/`: Directory containing HTML files for the login and registration pages.
- `database.db`: SQLite database file that stores user credentials.

## Routes

- **`/`**: Renders the login page.
- **`/authenticate`**: Handles authentication logic for logging in users.
- **`/register`**: Renders the registration page.
- **`/register_user`**: Handles the logic for registering a new user.
- **`/home`**: Redirects to the home page after successful login.

## Setup Instructions

1. Clone the repository to your local machine.
2. Ensure you have Python and Flask installed.
3. Run the following command to start the application:
    ```bash
    python app.py
    ```
4. Access the application by navigating to `http://127.0.0.1:5000/` in your web browser.

## Notes

- The SQLite database (`database.db`) will be created automatically when the application is run.
- This application uses plain text passwords, which is not secure for production environments. Consider hashing passwords before storing them in a real-world scenario.

## License

This project is licensed under the MIT License.
