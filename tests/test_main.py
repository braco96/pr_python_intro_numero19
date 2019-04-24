import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_redondear_json():
    d = {"a": 1, "b": [1,2,{"c":3}]}
    assert mod.redondear_json(d) == d
