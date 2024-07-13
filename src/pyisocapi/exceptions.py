class BadRequestError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class RateLimitedError(Exception):
    pass


class InternalServerError(Exception):
    pass


class UnknownStatusCodeError(Exception):
    pass


class InvalidPageNumberError(Exception):
    """Page number should be in range [1-inf]"""
