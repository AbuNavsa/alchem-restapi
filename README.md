# Python Project Repository

Welcome to the Python Project repository. This project is a Python application designed to be set up and run with ease. Follow the instructions below to get started.

## Prerequisites

Ensure you have the following software installed:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

check python version with `python --version` or `python3 --version`

## Setup Instructions

Follow these steps to set up the Python project repository:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AbuNavsa/alchem-restapi.git
   cd alchem-restapi

   ```

2. **Set Up a Virtual Environment**
   Can skip this step
   It's a best practice to use a virtual environment to manage your project’s dependencies. Create and activate a virtual environment with the following commands:

`python -m venv myenv` or `python3 -m venv myenv`
`source myenv/bin/activate`

3. **Install Requirements** `pip install -r requirements.txt`

4. **Create database**
   `python create_db.py` If this doesn't work, try python3 instead of python

5. **Run system data generator to fill table repeatedly** `python event_simulator.py`
   Keep this running whilst the UI is running as this is where the data comes from


6. **Run server** run `uvicorn main:app --reload` in a new terminal (make sure to enter your virtual environment again)

After this is running, head over to the Angular frontend and set up there. In conclusion, the event_simulator.py and server should be running.