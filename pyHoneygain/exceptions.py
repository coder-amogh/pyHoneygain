class HoneygainAPIError(Exception):
	"""Base Honeygain API Exception"""
	def __init__(self, *args: object) -> None:
		super().__init__(*args)

class NotLoggedInError(HoneygainAPIError):
	"""Raised when you're not logged in and try to access protected endpoints. """
	def __init__(self, *args: object) -> None:
		super().__init__(*args)

class UserConfirmationRequiredError(HoneygainAPIError):
	"""Raised when user confirmation is required. """
	def __init__(self, *args: object) -> None:
		super().__init__(*args)
