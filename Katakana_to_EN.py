import os
from pykakasi import kakasi

kakasi = kakasi()

kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
kakasi.setMode("C", True)

conv = kakasi.getConverter()

os.path.dirname(os.path.abspath(__file__))

bands = list()
path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(path)

for file in files:
    if file.endswith('.csv'):
        f = (path + '/' + file);

        with open (f) as org:
            for line in org:
                bands.append(conv.do(line.strip()).title().replace('　',' '))

        filename = path + '/' + 'Converted_' + file

        with open(filename, 'w') as result:
            for band in bands:
                result.write(band + '\n')