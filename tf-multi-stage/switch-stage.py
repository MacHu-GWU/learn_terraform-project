# -*- coding: utf-8 -*-

import os
import json

CONFIG_JSON_FILENAME_AT_HOME = "skymap-mpl-config.json"

here = os.path.dirname(__file__)
home = os.path.expanduser("~")
var_json = os.path.join(here, "var.json")
config_json = os.path.join(home, CONFIG_JSON_FILENAME_AT_HOME)

valid_stage = ["dev", "test", "qa", "stage", "prod"]


def switch(stage):
    if stage not in valid_stage:
        raise Exception("'{}' is not a valid stage name, it has to be one of {}!".format(stage, valid_stage))
    with open(config_json, "rb") as f:
        config_data = json.loads(f.read().decode("utf-8"))

        if stage not in config_data:
            raise Exception("'{}' is not ")

        var_data = config_data[stage]
        with open(var_json, "wb") as f:
            f.write(json.dumps(var_data, indent=4, sort_keys=True, ensure_ascii=False).encode("utf-8"))


if __name__ == "__main__":
    import sys

    stage = sys.argv[1]
    switch(stage)
