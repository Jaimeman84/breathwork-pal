# Breathwork Application

A modern breathwork application built with Python and Streamlit that provides various breathing techniques through interactive visualizations.

## Features

- Multiple breathing patterns:
  - Circle breathing for hold-breath exercises
  - Wave breathing for inhale/exhale patterns
- Customizable duration for each exercise
- Smooth animations and visual guidance
- Clean, modern interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/breathwork-app.git
cd breathwork-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Select your preferred breathing pattern and duration from the sidebar

4. Follow the animated guide for your breathing exercise

## Project Structure

The project follows SOLID principles and is organized as follows:

- `src/`: Source code directory
  - `breathing_patterns/`: Different breathing pattern implementations
  - `utils/`: Utility functions and helpers
  - `app.py`: Main Streamlit application
- `tests/`: Unit tests
- `requirements.txt`: Project dependencies

## Testing

Run the tests using pytest:
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.