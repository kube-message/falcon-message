#!/usr/bin/env bash
set -e

proto_dir=~/repos/kube/proto
alerts_python_out_dir=~/repos/kube/messenger/messenger/proto/alerts
messenger_venv=~/repos/kube/messenger/venv

$messenger_venv/bin/python -m grpc_tools.protoc -I $proto_dir --python_out=$alerts_python_out_dir --grpc_python_out=$alerts_python_out_dir $proto_dir/alerts.proto