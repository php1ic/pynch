# PyNCH - The Python Nuclear CHart

## Introduction

The Interactive Nuclear CHart ([INCH](https://github.com/php1ic/inch)) has been use to aggregate the nuclear mass tables produced by [NUBASE](http://amdc.in2p3.fr/web/nubase_en.html) & [AME](https://www-nds.iaea.org/amdc/) to create a [json](https://www.json.org/json-en.html) file.
This file format is trivially readable by python, after which the [dash](https://plotly.com/dash/) module has been used to create an interactive webpage to allow the user to interogate the data they are interested in.

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
The file was automatically created with [pipreqs](https://pypi.org/project/pipreqs/), hence why versions are assigned to all modules.
I am not aware of any version specific functionality that is used in this project.

## Running

With all of the necessary requirements installed, the below will start the app
```bash
python3 app.py
```
The console will tell you where to point your browser - likely http://127.0.0.1:8050/.

## Mass tables

The data files released by the papers linked below are used to create the mass tables read by this code
- [AME2003](http://www.sciencedirect.com/science/article/pii/S0375947403018086) + [NUBASE2003](http://www.sciencedirect.com/science/article/pii/S0375947403018074) = [masstable2003](./data/masstable2003.json)
- [AME2012](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract2709.shtml) + [NUBASE2012](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract2725.shtml) = [masstable2012](./data/masstable2012.json)
- [AME2016](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract8344.shtml) + [NUBASE2016](http://cpc-hepnp.ihep.ac.cn:8080/Jwk_cpc/EN/abstract/abstract8343.shtml) = [masstable2016](./data/masstable2016.json)

The NUBASE files are read for all of the data values, with the AME files being used to populate an additional mass excess data field.
No comparison or validation is done on common values.

## Additional uses

The [mass_data](mass_data) module uses [pandas](https://pandas.pydata.org/) to store the data and index by the year the table was published.
If you want to do your own thing with the data, you could import this module then sort, slice and filter the resultant dataframe to your heart's content.
