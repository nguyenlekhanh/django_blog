from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_domainonly_email(value):
    #if not "yourdomain.com" in value:
    #    raise ValidationError(_("Sorry, the email submitted is invalid."))
    return value

BLACKLIST = ['abc', 'test']
def validate_blacklisted(value):
    if value in BLACKLIST:
        raise ValidationError(_("Sorry, this value is not valid."))
    return value
