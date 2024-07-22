# Python Project Repository

Welcome to the Python Project repository. This project is a Python application designed to be set up and run with ease. Follow the instructions below to get started.

## Prerequisites

Ensure you have the following software installed:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

## Setup Instructions

Follow these steps to set up the Python project repository:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-python-repo.git
   cd your-python-repo

2. **Set Up a Virtual Environment**

It's a best practice to use a virtual environment to manage your project’s dependencies. Create and activate a virtual environment with the following commands:

`python -m venv venv`
`source venv/bin/activate`

3. **Install Requirements**

`pip install -r requirements.txt`

4. **Create database**
`python create_db.py` if this doesn't work, try python3 instead of python

5. **Run system data generator to fill table repeatedly**
6. 
`python event_simulator.py`

7. **Run server**
8. 
`uvicorn main:app --reload`

After this is running, head over to the Angular frontend and set up there

