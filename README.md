# PyNCH - The Python Nuclear CHart

[![Unit Tests](https://github.com/php1ic/pynch/actions/workflows/ci.yml/badge.svg)](https://github.com/php1ic/pynch/actions/workflows/ci.yml)

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
- [AME2003](http://www.sciencedirect.com/science/article/pii/S0375947403018086) + [NUBASE2003](http://www.sciencedirect.com/science/article/pii/S0375947403018074)
- [AME2012](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract2709.shtml) + [NUBASE2012](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract2725.shtml)
- [AME2016](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract8344.shtml) + [NUBASE2016](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract8343.shtml)

The NUBASE files are read for all of the data values, with the AME files being used to populate an additional mass excess data field.
No comparison or validation is done on common values.

## Additional uses

If you want to do your own thing with the data, you could import this module, access the `MassTable().full_data` dataframe, then sort, slice and filter the resultant dataframe to your heart's content.
