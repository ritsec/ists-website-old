"""
This module sets up the views for easy configuration in the application
factory.
"""
# Internal imports
from project.views import (
    root,
    fourteen,
    fifteen,
    archive,
)

# Pack views for registration.
views = [
    root.bp,
    fourteen.bp,
    fifteen.bp,
    archive.bp,
]
