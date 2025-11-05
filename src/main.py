import grpc
from concurrent import futures
import time
import os
import sys

# Add the gen directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'gen'))

# Import the generated gRPC code
from accounts_pb2_grpc import add_AccountsServiceServicer_to_server
from services.AccountsService import AccountsService

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add the service to the server
    add_AccountsServiceServicer_to_server(AccountsService(), server)
    
    # Listen on port 50051
    port = '50051'
    server.add_insecure_port('[::]:' + port)
    
    # Start the server
    print(f"Starting gRPC server on port {port}...")
    server.start()
    
    # Keep the server running
    try:
        while True:
            time.sleep(86400)  # One day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()