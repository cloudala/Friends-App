import os
import shutil
import re

# Define the source and destination directories
source_dir = 'episode_text_analysis/episode_analysis'
destination_dir = 'client/public'

# Define the pattern to match files
pattern = re.compile(r'season_\d+\.\d+_episode_\d+\.\d+_wordcloud')

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Iterate through the files in the source directory
for filename in os.listdir(source_dir):
    if pattern.match(filename):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")

print("File copy operation completed.")