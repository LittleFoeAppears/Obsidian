from wtforms import ValidationError

def validate_message_length(form, field):
    if len(field.data) < 10:
        raise ValidationError('Message must be at least 10 characters long')