import re

from django.core.signing import Signer, TimestampSigner, BadSignature, SignatureExpired
from django.utils.translation import gettext as _


def unsign_object(data, salt='', max_age=None):

    if max_age is not None and isinstance(max_age, int) is False:
        raise TypeError(_('max age must be of type int'))

    try:
        if max_age is not None:
            signer = TimestampSigner(salt)
            unsigned_data = signer.unsign_object(data, max_age=max_age)
        else:
            signer = Signer(salt)
            unsigned_data = signer.unsign_object(data)

    except SignatureExpired as e:
        return {'message': str(e)}

    except BadSignature as e:
        return {'message': str(e)}

    return {
        'data': unsigned_data,
        'max_age': max_age,
    }
