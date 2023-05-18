##
# Project Title
#
# @file
# @version 0.1
.PHONY: grpc
grpc:
	python -m grpc_tools.protoc -I./protobufs --python_out=./src/infrastructure/network/grpc --grpc_python_out=./src/infrastructure/network/grpc ./protobufs/*.proto
	@for file in src/infrastructure/network/grpc/*_pb2_grpc.py; do \
		sed -i 's/import \([a-zA-Z_]*\)_pb2 as \([a-zA-Z_]*\)__pb2/import infrastructure.network.grpc.\1_pb2 as \2__pb2/g' $$file ; \
	done
# end
