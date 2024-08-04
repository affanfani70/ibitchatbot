# ChatBot Project

This project is a Flask-based chatbot designed for providing information about the Institute of Business and Information Technology (IBIT) at Punjab University.

## Project Structure

- `app/`: Main application code.
  - `chatbot/`: Contains the chatbot logic and utilities.
  - `templates/`: HTML templates for the web interface.
  - `static/`: Static files like CSS and JavaScript.
  - `config.py`: Configuration settings.
  - `routes.py`: API route definitions.
- `data/`: Data files used by the chatbot.
- `tests/`: Unit tests for the project.
- `docs/`: Documentation files.
- `requirements.txt`: Python dependencies.
- `run.py`: Entry point to run the Flask app.

## How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set environment variables:
    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    ```

3. Run the app:
    ```bash
    flask run
    ```

## API Endpoints

- `/`: Home page.
- `/get_response`: POST endpoint to get a chatbot response.
- `/reload_data`: POST endpoint to reload the chatbot data.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.
