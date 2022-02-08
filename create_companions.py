###############################################################
# Examples of cell painting image files sent to IDR
# r02c02f01p01-ch1sk1fk1fl1.tiff
# r08c21f05p01-ch4sk1fk1fl1.tiff
# r02c02f01p01-ch2sk1fk1fl1.tiff
# r08c21f05p01-ch5sk1fk1fl1.tiff
# r02c02f01p01-ch3sk1fk1fl1.tiff
# r08c21f06p01-ch1sk1fk1fl1.tiff
# r02c02f01p01-ch4sk1fk1fl1.tiff
# r08c21f06p01-ch2sk1fk1fl1.tiff
# r02c02f01p01-ch5sk1fk1fl1.tiff
# r08c21f06p01-ch3sk1fk1fl1.tiff
# r02c02f02p01-ch1sk1fk1fl1.tiff
# r08c21f06p01-ch4sk1fk1fl1.tiff
# r02c02f02p01-ch2sk1fk1fl1.tiff
# r08c21f06p01-ch5sk1fk1fl1.tiff
# r02c02f02p01-ch3sk1fk1fl1.tiff
# r08c21f07p01-ch1sk1fk1fl1.tiff
# r02c02f02p01-ch4sk1fk1fl1.tiff
# r08c21f07p01-ch2sk1fk1fl1.tiff
#
# Where:
#   r (01-08) = row
#   c (01-12) = column
#   f (01-09) = field
#   p (01-21) = plane
#   ch (1-4)  = channel
#   sk, unknown
#   fk, unknown
#   fl, unknown
#
# - Unless you are dealing with time-lapse data, the timepoint logic that was used in the case 
# of the idr0092 submission is irrelevant 
# (https://github.com/IDR/idr0092-ostrop-organoid/tree/216beab0142aa4e4b44cc02a2d55dda96e0dc9eb/scripts)
# - Regarding the channel, the script below was dealing with RGB images which is also likely irrelevant
# - For each field of view, you will want to define an `Image`  with several channels, using `image. add_channel()`, 
# then loop over the channels to map the TIFF files to the relevant plane using `image.add_tiff()`. 
# - Although this is not the same type of data, I think this code [1], used in another submission, 
# achieves something similar.
#
# [1] https://github.com/IDR/idr0065-camsund-crispri/blob/11654471822e03d1be749a6594f981ba6a9b78e2/scripts/generate_companions.py#L210-L235
#

import sys
from ome_model.experimental import Plate, Image, create_companion
import subprocess

plate_name = sys.argv[1]
#plate_name = 'BR00109990'  ## e.g.

list_of_tiff_files = plate_name + "_files.txt"

filenames = []
with open(list_of_tiff_files) as fp:                         
    line = fp.readline()
    while line:
        filenames.append(line.strip())
        line = fp.readline()
        

columns = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18','19', '20', '21']  
rows = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'] 
fields = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
planes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18','19', '20', '21']  
channels = ['1', '2', '3', '4']
timepoints = ['0h']
print("Creating {}.companion.ome ...".format(plate_name))
plate = Plate(plate_name, len(rows), len(columns)) 
well_index = 0
options = {
    'DeltaTUnit': 'h',
}
for row_index, row in enumerate(rows):
    for column_index, column in enumerate(columns):
        well = plate.add_well(row, column)
        for field_index, field in enumerate(fields):
            image = Image(basename, 2080, 1552, 25, 3, 1, order="XYZTC", type="uint8")
            well.add_wellsample(well_index, image)
            well_index += 1
            for channel_index, channel in enumerate(channels):
                for plane_index, plane in enumerate(planes):
                    tiff_file = "r{}c{}f{}p{}-ch{}sk1fk1fl1.tiff".format(row, column, field, plane, channel) 
                    if tiff_file in filenames:
                        basename = "{}{}".format(row, column)
                        image.add_channel("0")
                        image.add_tiff(tiff_file, c=0, z=plane_index+1, t=0, planeCount=21)
                       # image.add_plane(c=0, z=plane_index+1, t=0, options = options)

                        
    
companion_file = "{}.companion.ome".format(plate_name)
create_companion(plates=[plate], out=companion_file)

# Indent XML for readability
proc = subprocess.Popen(
    ['xmllint', '--format', '-o', companion_file, companion_file],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE)
(output, error_output) = proc.communicate()

print("Done.")