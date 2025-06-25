# QA Login Automation Project

This project is part of my QA portfolio and demonstrates automated testing of a login form using Selenium and Python.

## 🔧 Technologies Used:

- Python 3.13
- Selenium WebDriver
- Pytest
- ChromeDriver

## 🧪 Covered Test Cases:

- ✅ Valid login with standard credentials
- ❌ Invalid login with incorrect password
- ⚠️ Login with an empty username field

## 🧱 Project Structure:

````

qa-login-automation/
├── pages/
│   └── login\_page.py
├── tests/
│   └── test\_login.py
├── conftest.py
├── requirements.txt
└── README.md


## ▶️ Running the Tests:

1. Create and activate a virtual environment:
```bash
    python -m venv venv
    .\venv\Scripts\activate
````

2. Install the dependencies:

```bash
    pip install -r requirements.txt
```

3. Run the tests:

```bash
    python -m pytest tests/
```

## 👀 Notes:

- `conftest.py` is used for centralized setup and teardown of the WebDriver.
- `WebDriverWait` is implemented to reduce flaky test behavior.
- The tests use the Page Object Model (POM) pattern for cleaner and more maintainable code.
- The project can be extended with a BasePage class, logging, failure screenshots, and more advanced features.

## ✨ Author:

MDautev

---
