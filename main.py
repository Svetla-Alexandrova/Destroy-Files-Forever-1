from pathlib import Path

root_dir = Path('destination')

for path in root_dir.glob('*.csv'):
  with open(path, 'wb') as file:
    # removes the text in files, makes them empty
    file.write(b'')
  # removes all files
  path.unlink()
    
  