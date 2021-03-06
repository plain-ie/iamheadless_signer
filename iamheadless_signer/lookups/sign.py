import re

from django.core.signing import Signer, TimestampSigner
from django.utils.translation import gettext as _


def sign_object(data, salt='', max_age=None):

    if max_age is not None and isinstance(max_age, int) is False:
        raise TypeError(_('max age must be of type int'))

    if max_age is not None:
        signer = TimestampSigner(salt)
    else:
        signer = Signer(salt)

    signed_data = signer.sign_object(data)

    return {
        'data': signed_data,
        'max_age': max_age
    }
