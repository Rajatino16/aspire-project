# Mini Aspire API

This is a mini-aspire API built using Python 3.12 and Flask. The API allows users to create loans, view their loans, and add repayments.
Postman Documentation: https://documenter.getpostman.com/view/8128762/2sA3QqhDSy

## Requirements

- Python 3.12
- Flask

## Installation

1. Clone the repository:

```sh
git clone https://github.com/your-repo/mini-aspire-api.git
cd mini-aspire-api
```

2. Create and activate a virtual environment
```sh
python -m venv aspire_venv
source aspire_venv/bin/activate  # On Windows use `aspire_venv\Scripts\activate`
```

3. Install the dependencies
```sh
pip install -r requirements.txt
```

4. Run the project
```sh
python run.py
```

5. Running Tests
```sh
python -m unittest tests.test_loan
```

## Project Structure
```sh
aspire-project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_loan.py
├── requirements.txt
├── run.py
└── README.md
```


