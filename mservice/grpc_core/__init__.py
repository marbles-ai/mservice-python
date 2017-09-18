from google.protobuf import empty_pb2
import grpc
import os
import logging
import discovery_pb2.py
import discovery_pb2_grpc.py


_logger = logging.getLogger(__name__)


def get_client_transport(stub_class, host, port):
    """Open a connection to the gRPC service endpoint

    Args:
        stub_class: A grpc endpoint definition (the stub).
        host: The host domain name. Set to local_host if running locally.
        port: The service port.

    Returns:
        A tuple of the client end-point stub and channel
    """
    channel = grpc.insecure_channel('%s:%u' % (host, port))
    stub = stub_class(channel)
    return stub, channel


def configure_endpoint(stub, configuration, timeout=120):
    """Configure a service endpoint asynchronously.

    :param client: The client end-point stub returned from get_client_transport()
    :param configuration: The configuration.
    :param timeout: optional timeout
    :return: A ConfigResult instance.
    """
    config_future = stub.configure.future(configuration, timeout)
    return config_future.result()


