"""Error Handling for AddressComplete package."""

# Response Errors

class ResponseError(Exception):
    """Base exception for response errors."""
    pass

class CountryInvalidError(ResponseError):
    """Country code is invalid."""
    def __init__(self):
        super().__init__("Country code is invalid")
        
class InvalidSearchTermError(ResponseError):
    """SearchTerm is invalid."""
    def __init__(self):
        super().__init__("SearchTerm is invalid")
        
class LanguagePreferenceInvalidError(ResponseError):
    """LanguagePreference is invalid."""
    def __init__(self):
        super().__init__("LanguagePreference is invalid")
        
class NoResponseError(ResponseError):
    """No response from the server."""
    def __init__(self):
        super().__init__("No response from the server")

class IDInvalidError(ResponseError):
    """ID is invalid."""
    def __init__(self):
        super().__init__("ID is invalid")


class NotAvailableError(ResponseError):
    """Exception raised when the data requested is not available for 
    your account."""
    def __init__(self, message):
        super().__init__(message)
        

# API Errors

class APIError(Exception):
    """Base exception for API errors returned by the web service."""
    pass


class UnknownError(APIError):
    """Unknown error."""
    def __init__(self):
        super().__init__("Unknown error")


class UnknownKeyError(APIError):
    """Unknown key."""
    def __init__(self):
        super().__init__("Unknown key")


class AccountOutOfCreditError(APIError):
    """Account out of credit."""
    def __init__(self):
        super().__init__("Account out of credit")


class IPNotAllowedError(APIError):
    """Request not allowed from this IP."""
    def __init__(self):
        super().__init__("Request not allowed from this IP")


class URLNotAllowedError(APIError):
    """Request not allowed from this URL."""
    def __init__(self):
        super().__init__("Request not allowed from this URL")


class ServiceNotAvailableOnKeyError(APIError):
    """Web service not available on this key."""
    def __init__(self):
        super().__init__("Web service not available on this key")


class ServiceNotAvailableOnPlanError(APIError):
    """Web service not available on your plan."""
    def __init__(self):
        super().__init__("Web service not available on your plan")


class KeyDailyLimitExceededError(APIError):
    """Key daily limit exceeded."""
    def __init__(self):
        super().__init__("Key daily limit exceeded")


class AccountSuspendedError(APIError):
    """Account has been suspended."""
    def __init__(self):
        super().__init__("Your account has been suspended")


class SurgeProtectorTriggeredError(APIError):
    """Surge protector triggered."""
    def __init__(self):
        super().__init__("Surge protector triggered")


class NoValidLicenseError(APIError):
    """No valid license available."""
    def __init__(self):
        super().__init__("No valid license available")


class ManagementKeyRequiredError(APIError):
    """Management key required."""
    def __init__(self):
        super().__init__("Management key required")


class DemoLimitExceededError(APIError):
    """Demo limit exceeded."""
    def __init__(self):
        super().__init__("Demo limit exceeded")


class FreeServiceLimitExceededError(APIError):
    """Free service limit exceeded."""
    def __init__(self):
        super().__init__("Free service limit exceeded")


class WrongKeyTypeError(APIError):
    """Wrong type of key."""
    def __init__(self):
        super().__init__("Wrong type of key")


class KeyExpiredError(APIError):
    """Key expired."""
    def __init__(self):
        super().__init__("Key expired")


class UserLookupLimitExceededError(APIError):
    """Individual User exceeded Lookup Limit."""
    def __init__(self):
        super().__init__("Individual User exceeded Lookup Limit")


class InvalidParametersError(APIError):
    """Missing or invalid parameters."""
    def __init__(self):
        super().__init__("Missing or invalid parameters")


class InvalidJSONError(APIError):
    """Invalid JSON object."""
    def __init__(self):
        super().__init__("Invalid JSON object")


class EndpointNotAvailableError(APIError):
    """Endpoint not available."""
    def __init__(self):
        super().__init__("Endpoint not available")


class SandboxNotAvailableError(APIError):
    """Sandbox Mode is not available on this endpoint."""
    def __init__(self):
        super().__init__("Sandbox Mode is not available on this endpoint")


class HTTPSRequiredError(APIError):
    """HTTPS requests only."""
    def __init__(self):
        super().__init__("HTTPS requests only")


class AgreementNotSignedError(APIError):
    """Agreement Not Signed."""
    def __init__(self):
        super().__init__("Agreement Not Signed")


