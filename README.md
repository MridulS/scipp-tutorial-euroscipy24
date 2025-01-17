# Multi-dimensional arrays with scipp

This tutorial provides a [pixi](https://pixi.sh/latest/) environment and if you already have pixi installed you can clone the repo and get started.
```
git clone https://github.com/MridulS/scipp-tutorial-euroscipy24
cd scipp-tutorial-euroscipy24
pixi install
pixi run setup_data # download nyc_taxi dataset
pixi run jupyter lab
```


pixi-inside-conda/mamba
```
git clone https://github.com/MridulS/scipp-tutorial-euroscipy24
cd scipp-tutorial-euroscipy24
mamba create -n pixi-test pixi
mamba activate pixi-test
pixi install
pixi run setup_data # download nyc_taxi dataset
pixi run jupyter lab
```


If you prefer using a conda/mamba environment you can get a local environment setup with:
```
git clone https://github.com/MridulS/scipp-tutorial-euroscipy24
cd scipp-tutorial-euroscipy24
mamba env create -f environment.yml
# download nyc_taxi dataset
curl "https://public.esss.dk/groups/scipp/dmsc-summer-school/scipp/nyc_taxi_data_2015_small.tar.gz" --output data/nyc_taxi_data_2015_small.tar.gz
python notebooks/utils/untar.py
jupyter lab
```

More in-depth tutorials are available in the [scipp user guide](https://scipp.github.io/user-guide/index.html).
