from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if filesize>1600000000:
        raise ValidationError('Maximum size to upload video is 200mb')