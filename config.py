"""
The production configuration file for the ISTS website.  The shown
configuration values are the defaults for the development deployment, and
should be changed.
"""
# Unique, secure secret key for the Flask web server.
SECRET_KEY = 'ExAwOlw3PwNWnZROXAEJaOFr1/ezy4C6LOASg7j58pU='

# The number of the upcoming ISTS event.
ISTS_NUMBER = '17'

# The year in which the next ISTS will happen.
YEAR = '2019'

# The month in which the next ISTS will happen.
MONTH = 'February'

# The day of the month of the set-up day for the next ISTS.
SETUP_DAY = '22'

# The day of the month of the first competition day for the next ISTS.
FIRST_DAY = '23'

# The day of the month of the second competition day for the next ISTS.
SECOND_DAY = '24'

# The main room in which the next ISTS will be held.
ROOM = 'USC-1600'

# Whether or not registration for blue teams is open for the next ISTS.
BLUE_REG_OPEN = False

# The link for blue team registration for the next ISTS.
BLUE_REG_LINK = 'http://blueteam-ists.ritsec.club'

# The link for white team registration for the next ISTS.
WHITE_REG_LINK = 'http://whiteteam.ritsec.club'

# The contact email for more information about non-RIT blue team information.
CONTACT_EMAIL = 'ritsecclub@gmail.com'
