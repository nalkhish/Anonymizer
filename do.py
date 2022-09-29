def execute():
  import os
  import uuid
  import csv
  from tkinter import filedialog

  # get directory name
  target_dir = filedialog.askdirectory()

  # get file names
  files = []
  for f in os.listdir(target_dir):
    temp = target_dir + "\\" + f
    if os.path.isfile(temp):
      files.append(f)


  # write a csv file
  with open(target_dir + '\\rename_map.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Old name', 'New name'])
    
    # rename files and write the rows
    for f in files:
      try:
        old_name = f
        new_name = f"{str(uuid.uuid4())}.txt"
        # rename
        os.rename(target_dir + "\\" + f, target_dir + "\\" + new_name)
        # record having written
        csv_writer.writerow([old_name, new_name])
        print(f"successfully renamed {old_name} to {new_name}")
      except Exception as e:
        print(f"Exception - {e}")





