# UI Automation Testing Project (Web)

This project contains a framework for UI automation testing on Web and Mobile (Android) platforms. The framework is built using Python with Pytest as the test runner, Selenium for browser interaction, and Appium for mobile device interaction.

## Project Structure
```
pytestweb/
├── web/                    # All Web testing related code
│   ├── config/             # Selenium & browser configuration
│   ├── locators/           # UI element locators
│   ├── pages/              # Page Objects implementation
│   └── tests/              # Test scripts
├── reports/                # Output directory for test reports
│   ├── allure/
│   └── html/
├── test_data/              # Data files for testing (e.g., JSON)
├── utils/                  # Utilities and helper functions
├── conftest.py             # Global Pytest fixtures & configuration
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/arkage88/pytestweb
cd pytestweb
```

### 3. Install Python Dependencies
Install all required Python packages from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the project's root directory. Copy the content below and adjust the values as needed. This file is used to store sensitive and environment-specific configurations.


## Running Tests
Ensure the Appium server is running for mobile tests.

### Running All Tests
```bash
pytest
```

### Running Web Tests
```bash
pytest web/tests
```


