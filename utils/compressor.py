import os
import subprocess
import zipfile
import zstandard as zstd
from PIL import Image
from utils.file_type import detect_file_type

# Extensions considered already compressed
compressed_exts = [
    ".exe", ".zip", ".jpg", ".jpeg", ".png", ".mp4", ".mp3", ".pdf"
]

def compress_file(file_path):
    file_type = detect_file_type(file_path)
    file_ext = os.path.splitext(file_path)[1].lower()
    warning = None

    if file_ext in compressed_exts:
        warning = "This file type is already compressed. Compression may not reduce size."

    if file_type == "video":
        output = file_path.replace(".", "_compressed.")
        cmd = ["ffmpeg", "-i", file_path, "-vcodec", "libx265", "-crf", "28", output]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    elif file_type == "audio":
        output = file_path.replace(".", "_compressed.")
        cmd = ["ffmpeg", "-i", file_path, "-codec:a", "libmp3lame", "-qscale:a", "4", output]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    elif file_type == "image":
        output = file_path.replace(".", "_compressed.")
        img = Image.open(file_path)
        img.save(output, "WEBP", quality=50)

    else:
        output = file_path + ".zst"
        with open(file_path, 'rb') as f_in, open(output, 'wb') as f_out:
            cctx = zstd.ZstdCompressor(level=10)
            cctx.copy_stream(f_in, f_out)

    return output, warning