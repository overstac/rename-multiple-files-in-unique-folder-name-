from pathlib import Path

root_dir= Path("files")
file_paths = root_dir.glob("**/*")

#schema 1
for path in file_paths:
  if path.is_file():
    an_folder= path.parts[-3]
    luna_folder = path.parts[-2]

    new_name= an_folder + "-" + luna_folder + "-" + path.name
    print(new_name)
    new_filepath= path.with_name(new_name)
    path.rename(new_filepath)


schema 2
for path in file_paths:
  if path.is_file():
    nume_despartit = path.parts
    an_si_luna= path.parts[1:-1]

    new_name= "-".join(an_si_luna) + "-" + path.name
    print(new_name)
    new_filepath= path.with_name(new_name)
    path.rename(new_filepath)





