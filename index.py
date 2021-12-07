import os

files = os.listdir("/Volumes/GoogleDrive/My Drive/Notes/pages")

final_output = ""

# Create Formatted Index
for file in files:
    split_file = os.path.splitext(file)
    if split_file[1] == ".md":
        file_link = f'[{split_file[0]}]({file})\n\n'
        final_output += file_link

# Write Output to File
with (open('index.md', 'w')) as f:
    f.write(final_output)

