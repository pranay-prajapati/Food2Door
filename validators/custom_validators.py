from abc import ABC, abstractmethod
from wtforms.validators import ValidationError


class CustomValidator(ABC):
    """
    Interface for custom validator for Flask Form.
    """

    def __init__(self, message=None):
        self.message = message

    @abstractmethod
    def __call__(self, form, field):
        raise NotImplementedError("Abstract method.")


class PasswordValidator(CustomValidator):
    """
    Custom validator for Flask Form. Checks if password is correct.
    """

    def __init__(self, min_len=8, message="Invalid password"):
        self.min_len = min_len
        super().__init__(message=message)

    def __call__(self, form, field):
        password = field.data
        if len(password) < self.min_len:
            raise ValidationError("Your new password must be more than 8 characters.")