#!/usr/bin/env python3
"""
Instatiates a Babel Object
"""


from flask_babel import Babel

babel = Babel(app)


class Config:
    """
    Class Config
    """
    LANGUAGES = ["en", "fr"]
