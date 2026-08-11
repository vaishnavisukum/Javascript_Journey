import os

folder_path = r"C:\Users\Vaishnavi Sukum\Desktop\GenX"

file_count = 0

for root, dirs, files in os.walk(folder_path):
    file_count += len(files)

print("Total files:", file_count)