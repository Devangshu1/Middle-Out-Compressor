import sys
import os
from utils.file_type import detect_file_type
from utils.compressor import compress

def main(file_path):
    if not os.path.exists(file_path):
        print("❌ File does not exist!")
        return

    file_type = detect_file_type(file_path)
    print(f"🔍 Detected file type: {file_type}")
    output_file, ratio = compress(file_path, file_type)

    print(f"✅ Compressed File: {output_file}")
    print(f"📉 Compression Ratio: {ratio:.2f}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
    else:
        main(sys.argv[1])
