#! /bin/bash

# Prepares the build environment

PROTOC=$(which protoc)
PYPLUGIN=$(which grpc_python_plugin)
pushd $(dirname $0) > /dev/null
PROJDIR=$PWD
popd > /dev/null

if test "x$PROTOC" == "x"; then
    echo "Missing protoc compiler"
    exit 1
elif test "x$PYPLUGIN" == "x"; then
    echo "Missing grpc_python_plugin compiler"
    exit 1
fi

OUTDIR=$PROJDIR/mservice/grpc_core
PROTOFILES=$(find $PROJDIR/proto -name '*.proto' -type f)

CMD="$PROTOC --python_out=$OUTDIR -I$PROJDIR/proto --grpc_out=$OUTDIR --plugin=protoc-gen-grpc=$PYPLUGIN $PROTOFILES"
echo $CMD
$CMD

