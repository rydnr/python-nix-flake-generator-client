##
# Project Title
#
# @file
# @version 0.1
.PHONY: grpc
grpc:
	python -m grpc_tools.protoc -I./protobufs --python_out=. --grpc_python_out=. ./protobufs/*.proto
# end
