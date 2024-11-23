import magic, pypandoc

async def convert(file: bytes):
    pass

async def check_type(file: bytes):
    mime = magic.from_buffer(file)
    if mime.find("PDF") == -1:
        return convert(file)
    else:
        return file
