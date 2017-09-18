# Service support for python

Core stuff for python services and gRPC endpoints. The gRPC proto files are located in submodule [proto](./proto). 
The base gRPC service interfaces are included with the wheel.

## Cloning
This project links to a protobuf submodule. After cloning this project you must run:
```
git submodule init
git submodule update
```

Alternatively you can do this when you clone:
```
git clone --recursive https://github.com/marbles-ai/mservice-python.git
```

## Building the wheel
The wheel output will be located at `./dist`. The release flag can optionally build proto endpoints, or set the version,
before running the script. You can also build the proto's once by running `./init.sh`. 
```
python setup.py [release --proto|version=<V.R.B>]
```

## Uploading wheel to Github

Wheels are stored on our github repository. 
Make sure you tag with the version each time you upload.

## TODO
1. Add a script to increment version, tag, and upload wheel.

