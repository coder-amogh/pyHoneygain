class NotLoggedInError(Exception):
	"""Raised when you're not logged in and try to access protected endpoints. """
	pass

class UserConfirmationRequiredError(Exception):
	"""Raised when user confirmation is required. """
	pass
