import os
os.system("pdftk a.pdf burst output output_%02d.pdf compress")