# Breathwork Pal 🌬️

A modern, interactive breathwork application built with Python and Streamlit that provides various breathing techniques through animated visual patterns. The app helps users practice different breathing exercises with clear visual guidance.

## Features

### Breathing Patterns
- **Circle Breathing**: Follow the dot around a circle for hold-breath exercises
- **Wave Breathing**: Follow the wave pattern for basic inhale/exhale techniques
- **Square Breathing**: Box breathing technique (inhale, hold, exhale, hold)

### Interactive Elements
- Animated dot movement following breathing patterns
- Clear start (green star) and end (red star) points
- Real-time phase indicators
- Progress tracking and remaining time display
- Adjustable duration and animation speed
- Play/Pause and Reset controls

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jaimeman84/breathwork-pal.git
cd breathwork-pal
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
```
breathwork-pal/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── breathing_patterns/
│   │   ├── __init__.py
│   │   ├── base_pattern.py
│   │   ├── circle_pattern.py
│   │   ├── wave_pattern.py
│   │   └── square_pattern.py
│   └── config.py
└── tests/
    ├── __init__.py
    ├── test_patterns.py
    └── test_timer.py
```

## Dependencies
- streamlit>=1.31.0
- numpy>=1.24.3
- plotly>=5.18.0
- pytest>=7.4.0

## Usage

1. Run the application:
```bash
streamlit run src/app.py
```

2. Using the app:
   - Select a breathing pattern from the sidebar
   - Adjust duration (30-300 seconds) and animation speed
   - Click 'Start' to begin the exercise
   - Follow the blue dot, starting from the green star
   - Use 'Pause' to pause anytime
   - Use 'Reset' to start over

### Pattern Guide
- **Circle Breathing**: Continuous hold breath exercise
- **Wave Breathing**: Inhale as dot moves up, exhale as it moves down
- **Square Breathing**: 
  - Bottom to Top: Inhale
  - Right side: Hold
  - Top to Bottom: Exhale
  - Left side: Hold

## Development

### Running Tests
```bash
pytest tests/
```

### Project Architecture
- Follows SOLID principles
- Uses abstract base class for patterns
- Implements clean architecture with separation of concerns
- Includes comprehensive unit tests

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Safety Note

Always breathe at a comfortable pace. If you experience any discomfort, stop the exercise and return to normal breathing. Consult a healthcare professional before starting any breathing practice.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by modern breathwork applications and meditation practices
- Built with Streamlit's interactive features
- Visualization powered by Plotly