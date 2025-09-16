
class FunctionCallError(Exception):
    """Exception raised for errors in the function calls."""
    def __init__(self, message: str = "Error occurred during function call."):
        super().__init__(message)
        self.message = message

class ModelUnavailableError(Exception):
    """Exception raised when no models are available."""
    def __init__(self, message: str = "No available models at the moment. Please try again later."):
        super().__init__(message)
        self.message = message