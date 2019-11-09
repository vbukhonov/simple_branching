import os


def upload_facade_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "{}_facade.{}".format(
        instance.name,
        filename_ext.lower(),
    )
