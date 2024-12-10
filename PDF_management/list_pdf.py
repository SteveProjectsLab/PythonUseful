import os

all_files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".pdf")]:
        all_files.append(os.path.join(dirpath, filename))
print(all_files)