import mimetypes

def detect_file_type(file_path):
    mime, _ = mimetypes.guess_type(file_path)
    if mime is None:
        return "other"
    if mime.startswith("video"):
        return "video"
    elif mime.startswith("audio"):
        return "audio"
    elif mime.startswith("image"):
        return "image"
    elif mime.startswith("application/pdf") or mime.startswith("text"):
        return "document"
    else:
        return "other"
