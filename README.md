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

If you want to do your own thing with the data, you could install this package, import this module, access `MassTable().full_data`, then sort, slice and filter the resultant dataframe to your heart's content. You can install this package with `pip install git+<package-repo>` where `<package-repo>` is the git repository of this package.

For example, track how the accuracy of the mass excess of 18B changes once it is experimentally measured
```python
>>> import pynch.mass_table as mt
>>> df = mt.MassTable().full_data
>>> df[(df['A'] == 18) & (df['Z'] == 5)][['Experimental', 'NubaseMassExcess', 'NubaseMassExcessError', 'NubaseRelativeError', 'DiscoveryYear']]
           Experimental  NubaseMassExcess  NubaseMassExcessError  NubaseRelativeError  DiscoveryYear
TableYear
2003              False           52320.0                  800.0             0.015291           1900
2012               True           51850.0                  170.0             0.003279           2010
2016               True           51790.0                  200.0             0.003862           2010
2020               True           51790.0                  200.0             0.003862           2010
```
Or for all of the A=100 isotopes from the 2012 table that have a mass-excess error < 10.0keV, print the A, Z, symbol and year of discovery 
```python
>>> import pynch.mass_table as mt
>>> df = mt.MassTable().full_data
>>> df.query('TableYear == 2012 and A == 100 and NubaseMassExcessError < 10.0')[['A', 'Z', 'Symbol', 'DiscoveryYear']]
             A   Z Symbol  DiscoveryYear
TableYear
2012       100  40     Zr           1970
2012       100  41     Nb           1967
2012       100  42     Mo           1930
2012       100  43     Tc           1952
2012       100  44     Ru           1931
2012       100  47     Ag           1970
2012       100  48     Cd           1970
```
Or how does the NUBASE mass-excess compare with the AME value for experimentally measured isotopes from the latest table? Which are the 10 isotopes with the biggest differences?
```python
>>> import pynch.mass_table as mt
>>> df = mt.MassTable().full_data
>>> # Create a new column comparing the measured values
>>> df['NUBASE-AME'] = df['NubaseMassExcess'] - df['AMEMassExcess']
>>> # Extract the data for measured isotopes and from the latest table
>>> df_comparison = df.query('TableYear == 2020 and Experimental == True')
>>> # Sort the difference in measured data by absolute value and print the columns we are interested in
>>> df_comparison.sort_values(by=['NUBASE-AME'], key=abs, ascending=False)[['A', 'Z', 'Symbol', 'NubaseMassExcess', 'AMEMassExcess', 'NUBASE-AME']].head(n=10)
             A   Z Symbol  NubaseMassExcess  AMEMassExcess  NUBASE-AME
TableYear
2020       221  91     Pa           20370.0      20374.937      -4.937
2020        57  23      V          -44440.0     -44435.063      -4.937
2020       102  50     Sn          -64930.0     -64934.896       4.896
2020       168  75     Re          -35790.0     -35794.889       4.889
2020       209  89     Ac            8840.0       8844.887      -4.887
2020       241  93     Np           54320.0      54315.115       4.885
2020       121  56     Ba          -70740.0     -70744.847       4.847
2020       122  55     Cs          -78140.0     -78144.769       4.769
2020       206  89     Ac           13480.0      13484.754      -4.754
2020        23   9      F            3290.0       3285.263       4.737
```
These are slightly contrived examples, but hopefully you get the idea. The data can be manipulated and added to as required.
