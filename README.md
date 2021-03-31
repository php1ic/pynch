# PyNCH - The Python Nuclear CHart

[![Unit Tests](https://github.com/php1ic/pynch/actions/workflows/ci.yml/badge.svg)](https://github.com/php1ic/pynch/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/php1ic/pynch/branch/master/graph/badge.svg?token=0OW8G0HYVG)](https://codecov.io/gh/php1ic/pynch)

## Introduction

The nuclear mass tables produced by [NUBASE](http://amdc.in2p3.fr/web/nubase_en.html) and [AME](https://www-nds.iaea.org/amdc/) are parsed into pandas dataframes.
These dataframes are then read with the [dash](https://plotly.com/dash/) module to create an interactive webpage to allow the user to interogate the data they are interested in.

No guarantee is supplied with regards to the accuracy of the data presented.
Estimated values are included, please always refer to the original sources.
All data should, however, be accurate.

Additional functionality and polish will be added as I learn more about [dash](https://plotly.com/dash/).
In the meantime, suggestions are welcome via [issues](https://github.com/php1ic/pynch/issues) or a pull request.

## Setup

As is the standard, you can confirm you have the necessary modules using the [requirements.txt](./requirements.txt) file
```bash
pip install --user -r requirements.txt
```

## Running

With all of the necessary requirements installed, the below will start the app
```bash
python3 app.py
```
The console will tell you where to point your browser - likely http://127.0.0.1:8050/.

## Mass tables

The data files released by the papers linked below are used to create the mass tables read by this code
- [AME2003](https://doi.org/10.1016/j.nuclphysa.2003.11.002) + [NUBASE2003](https://doi.org/10.1016/j.nuclphysa.2003.11.001)
- [AME2012](https://doi.org/10.1088/1674-1137/36/12/002) + [NUBASE2012](https://doi.org/10.1088/1674-1137/36/12/001)
- [AME2016](https://doi.org/10.1088/1674-1137/41/3/030002) + [NUBASE2016](https://doi.org/10.1088/1674-1137/41/3/030001)
- [AME2020](https://doi.org/10.1088/1674-1137/abddaf) + [NUBASE2020](https://doi.org/10.1088/1674-1137/abddae)

The NUBASE files are read for all of the data values, with the AME files being used to populate an additional mass excess data field.
No comparison or validation is done on common values.

## Additional uses

If you want to do your own thing with the data, you could import this module, access `MassTable().full_data`, then sort, slice and filter the resultant dataframe to your heart's content.
