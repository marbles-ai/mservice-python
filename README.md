# Marbles deployment

Core stuff for python services, gRPC and AWS. The gRPC proto files are located at submodule [proto](./proto). 
The base gRPC service interfaces are built for python and included with the package.  This allows us to control gRPC 
deployment from a python script.

Currently we only use AWS however we can add other service providers to this package.

## Cloning
This project links to a protobuf submodule. After cloning this project you must run:
```
git submodule init
git submodule update
```

Alternatively you can do:
```
git clone --recursive https://github.com/marbles-ai/marbles-proto.git
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

