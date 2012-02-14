MCS provides a single, simple Python function to import data from a Multi Channel Systems .mcd recording to a numpy array.

The .mcd file must be converted to a binary format using Multi Channel Systems' MC_DataTool:
http://www.multichannelsystems.com/downloads.html

Using the GUI, select your .mcd file, click the bin button, select your electrodes of interest and save.
IT IS IMPERATIVE THAT A HEADER BE INCLUDED.

Using the command line, you can construct a file like MassConvert.txt (included). 
Run this with MC_DataTool -file MassConvert.txt -bin -WriteHeader
As of MC_DataTool version 2.6.6, the documentation says one can include the -bin and -WriteHeader options in the command file itself, and not directly when entering the command. THIS IS NOT TRUE.

You will now have a .raw file, which can be imported into numpy with:

import MCS
data, sampling_rate, channel_names = MCS.import(file_name)

The data is a channels*time array, with the channels having the same order as channel_names.

The data will use the header data in the .raw file to set the appropriate level and scale for Electrode data. 

All data will now be float, though the data was originally stored in the .mcd as integers. This could have some implications for the numerical accuracy of the data, which should be totally irrelevant for the typical use cases of Multi Channel Systems' hardware.
