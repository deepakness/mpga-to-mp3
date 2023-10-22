# Bulk Convert MPGA Audio Files to MP3

Python code to easily convert `.mpga` audio files to `.mp3` format in bulk. The code can handle 100s and even 1000s of MPGA audio files to MP3 saved on your local computer.

![Bulk Convert MPGA Audio Files to MP3](/screenshot.jpg)

Here's how you can run the code on your computer:

## 1. Create the `app.py` file

Open the folder where all your `.mpga` files are stored in the VS Code and create a file `app.py` in the same folder and copy paste the following code inside the file:

```python
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
```

## 2. Install the `pydub` library

Open the terminal and run the following command to install the `pydub` library:

```
pip install pydub
```

## 3. Run the code

Now, run the code by running the following command:

```
python app.py
```

> Note that, depending upon the Python version and setup on your computer, you may need to use `pip3` and `python3` instead of `pip` and `python` when running the code.

After running the code, your audio files will start getting converted from `.mpga` to `.mp3` file format and the `.mp3` files are saved inside `/mp3` folder inside the main folder.

You can learn more about the process in [this blog post](https://deepakness.com/blog/mpga-to-mp3/).
