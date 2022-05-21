from email_validator import EmailNotValidError, validate_email


def length(min=0, max=1000):
    def validate(data):
        if len(data) < min:
            raise ValueError(f'String length must be at least {min} characters')
        if len(data) > max:
            raise ValueError(f'String length must be {max} characters or less')
        return data
    return validate


def email(data):
    return validate_email(data).email
