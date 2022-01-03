from concurrent import futures
import logging

import grpc
import python_sse_pb2
import python_sse_pb2_grpc


class SSE(python_sse_pb2_grpc.PythonServiceServicer):

    def testPython(self, request, context):
        return python_sse_pb2.Reply(message='test successful')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    python_sse_pb2_grpc.add_PythonServiceServicer_to_server(SSE(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
