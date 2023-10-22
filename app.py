import os
import shutil
from pydub import AudioSegment

def convert_mpga_to_mp3(file_path):
    try:
        # Load the .mpga file
        song = AudioSegment.from_file(file_path, "mp3")

        # Convert to mp3 and export
        new_file_path = file_path.rstrip(".mpga") + ".mp3"
        song.export(new_file_path, format="mp3")

        print(f"Converted {file_path} to {new_file_path}")

        return new_file_path
    except Exception as e:
        print(f"Failed to convert {file_path} due to error: {e}")
        return None


# Get all mpga files in the current directory
mpga_files = [f for f in os.listdir('.') if f.endswith('.mpga')]

# Create an 'mp3' directory if it doesn't exist
if not os.path.exists('mp3'):
    os.makedirs('mp3')

# Convert all mpga files
for file_path in mpga_files:
    new_file_path = convert_mpga_to_mp3(file_path)
    if new_file_path is not None:
        # Move the mp3 file to the 'mp3' directory
        try:
            shutil.move(new_file_path, 'mp3/')
            print(f"Moved {new_file_path} to mp3/ directory")
        except Exception as e:
            print(f"Failed to move {new_file_path} due to error: {e}")
