# MakersBnB Python Project 
Introducing MakersBNB by HugsForBugs! Our team, comprised of Lydia Ntafa, Gemma McKenzie, Fahim Islam, and Asha Ali, brings you this web app project developed during our time at Makers. With MakersBNB, you can effortlessly list your available spaces and book accommodations for overnight stays.

## Setup

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit http://localhost:5000/index in your browser
```
