"""Error Handling for AddressComplete package."""

class InvalidIDError(Exception):
    """Exception raised for invalid address IDs."""
    def __init__(self, message):
        super().__init__(message)
        
class NotAvailableError(Exception):
    """Exception raised when the data requested is not available for 
    your account"""
    def __init__(self, message):
        super().__init__(message)
        
