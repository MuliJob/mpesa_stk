"""Errors model"""
from enum import Enum

class PaymentErrorCode(Enum):
    """Handling errors which might occur"""
    INVALID = "invalid_phone"
    PAYMENT_ERROR = "payment_error"
