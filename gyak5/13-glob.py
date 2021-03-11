import glob
import os

# for file_name in glob.glob('csv_fajlok/netflix_yearly_data/**/*.csv'):
for file_name in glob.glob('csv_fajlok/netflix_yearly_data/*.csv'):
    print(file_name)
    print(os.path.abspath(file_name))

    # szetvalasztas evtizedekre
