from pathlib import Path
import yaml


class ConfigLoader:

    def __init__(self):

        config_path = Path(__file__).parent / "simulation.yaml"

        with open(config_path, "r") as f:

            self.config = yaml.safe_load(f)

    def get(self):

        return self.config


config = ConfigLoader().get()
