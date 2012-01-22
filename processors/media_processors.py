from django.conf import settings

class ImageResize:
    @staticmethod
    def process(resource):
        from PIL import Image

        i = Image.open(resource.source_file.path)
        if i.mode != 'RGBA':
                i = i.convert('RGBA')
        i.thumbnail(
            (settings.RESIZE_MAX_WIDTH, settings.RESIZE_MAX_HEIGHT),
            Image.ANTIALIAS
        )

        orig_path, _, orig_extension = resource.source_file.path.rpartition('.')
        if "RESIZE_FILENAME_POSTFIX" in dir(settings):
            postfix = settings.RESIZE_FILENAME_POSTFIX
        else:
            postfix = "-thumb"
        resize_path = "%s%s.%s" % (orig_path, postfix, orig_extension)

        if i.format == "JPEG" and "RESIZE_JPEG_QUALITY" in dir(settings):
            i.save(resize_path, quality = settings.RESIZE_JPEG_QUALITY, optimize = True)
        else:
            i.save(resize_path)
