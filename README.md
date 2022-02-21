# idr_ome_create
Python code that creates the companion.ome files, which are used by Omero/Bioformats to find out which TIFF files to assemble and how they are meant to be assembled.

Need:
1. execute "pip install ome_model"
2. a text file with listing of TIFF files, e.g., a file called "BR00109990_files.txt" that
contains file names:
    r02c02f01p01-ch1sk1fk1fl1.tiff
    r08c21f05p01-ch4sk1fk1fl1.tiff
    r02c02f01p01-ch2sk1fk1fl1.tiff
    r08c21f05p01-ch5sk1fk1fl1.tiff
    r02c02f01p01-ch3sk1fk1fl1.tiff
    r08c21f06p01-ch1sk1fk1fl1.tiff
    r02c02f01p01-ch4sk1fk1fl1.tiff
    r08c21f06p01-ch2sk1fk1fl1.tiff
    r02c02f01p01-ch5sk1fk1fl1.tiff
    r08c21f06p01-ch3sk1fk1fl1.tiff
    r02c02f02p01-ch1sk1fk1fl1.tiff
    r08c21f06p01-ch4sk1fk1fl1.tiff
    r02c02f02p01-ch2sk1fk1fl1.tiff
    r08c21f06p01-ch5sk1fk1fl1.tiff
    r02c02f02p01-ch3sk1fk1fl1.tiff
    r08c21f07p01-ch1sk1fk1fl1.tiff
    r02c02f02p01-ch4sk1fk1fl1.tiff
