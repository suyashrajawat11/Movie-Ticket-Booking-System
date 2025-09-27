class APIError(Exception):
    """Base exception for API errors"""
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = 'error'
        return rv

class ValidationError(APIError):
    """Raised when validation of request data fails"""
    def __init__(self, message, field=None, status_code=400, payload=None):
        super().__init__(message, status_code, payload)
        self.field = field

    def to_dict(self):
        rv = super().to_dict()
        if self.field:
            rv['field'] = self.field
        return rv

class NotFoundError(APIError):
    """Raised when a requested resource is not found"""
    def __init__(self, message='Resource not found', status_code=404, payload=None):
        super().__init__(message, status_code, payload)

class ConflictError(APIError):
    """Raised when there's a conflict with the current state of the resource"""
    def __init__(self, message='Conflict with the current state of the resource', status_code=409, payload=None):
        super().__init__(message, status_code, payload)

class UnauthorizedError(APIError):
    """Raised when authentication is required or has failed"""
    def __init__(self, message='Unauthorized', status_code=401, payload=None):
        super().__init__(message, status_code, payload)

class ForbiddenError(APIError):
    """Raised when the user doesn't have permission to access the resource"""
    def __init__(self, message='Forbidden', status_code=403, payload=None):
        super().__init__(message, status_code, payload)
