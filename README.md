# auto-json
auto-json is meant to quickly produce the files needed to run [barb](https://github.com/MorganWaddy/barb "barb"), the bayesian rate estimation package for FRBs. <br />

## Installation
```bash
git clone https://github.com/MorganWaddy/auto-json
```

## Creating Files
First, locate the needed values:
* First author of paper
* Year of publishing for the paper
* Number of FRBs recovered from the data
    * If none, or a nondetection, enter 0
* Sensitivity of the observation (in Janskys)
* Radius of telescope beam
* Number of beams
* Time per beam
* Flux of FRBs
    * If there were no FRBs recovered, enter -1

Create a json file with the relevant data
```bash
python bin/auto-json.py -N <name of primary author of the paper> -Y <year> -n <nFRBs> -S <sensitivity> -R <radius of the beam> -b <beams> -t <time per beam> -f <flux>
```

## Requirements
* argparse
* sys
