# scripts/make_protos.py
import subprocess

subprocess.run(["make", "grpc"], check=True)
