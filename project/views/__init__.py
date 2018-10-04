"""
This module sets up the views for easy configuration in the application
factory.
"""
# Internal imports
from project.views import root

# Pack views for registration
views = [
    root.bp,
]
