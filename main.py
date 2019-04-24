# -*- coding: utf-8 -*-
import re
import json

def redondear_json(d):
    return json.loads(json.dumps(d, ensure_ascii=False))

