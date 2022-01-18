# -*- coding: utf-8 -*-

import fsutil
import json


def read_json(filepath):
    return json.loads(fsutil.read_file(fsutil.join_path(__file__, filepath)))


def slugify(s):
    return s.lower().replace(" ", "-")
