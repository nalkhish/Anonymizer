def execute():
  import os
  import csv

  from tkinter import filedialog

  # get directory
  target_dir = filedialog.askdirectory()

  # open the rename map
  with open(target_dir + '\\rename_map.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
      try:
        renamed_name = row[1]
        old_name = row[0]
        # rename
        os.rename(target_dir + "\\" + renamed_name, target_dir + "\\" + old_name)
        print(f"successfully renamed {renamed_name} to {old_name}")
      except Exception as e:
        print(f"Exception - {e}")

