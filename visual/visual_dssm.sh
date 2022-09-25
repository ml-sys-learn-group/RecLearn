#!/bin/bash

python -m tf2onnx.convert --saved-model ../dssm_model --output dssm_model.onnx
netron 