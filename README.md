# Todo Web Application

This is a simple todo web application built using Flask framework for the backend and MySQL database for storage.

## Features

- **Task Management**: Allows users to create, read, update, and delete tasks.
- **User Authentication**: Option for user registration and login to manage tasks securely.
- **Database Integration**: Stores tasks in a MySQL database.
- **Simple and Intuitive Interface**: Designed for ease of use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sayan14banerjee/Todo-web-application.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Todo-web-application
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
   - Ensure you have MySQL installed and running locally.
   - Create a new database for the application.

5. Configure the database connection:
   - Update the database connection details in `app.py` file.

6. Run the application:
   ```bash
   python app.py
   ```

## Directory Structure

- **`__pycache__`**: Python bytecode cache directory.
- **`templates`**: HTML templates.
- **`app.py`**: Entry point of the Flask application.
- **`procfile`**: Configuration file for deploying on platforms like Heroku.
- **`requirements.txt`**: File containing the list of dependencies.

## Usage

1. Once the application is running, open your web browser and navigate to the specified address.
2. Register a new user account or login if you already have one.
3. Create, read, update, and delete tasks as needed.
4. Log out when finished.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
