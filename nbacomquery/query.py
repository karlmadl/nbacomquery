import requests
import pandas as pd
from nbacomquery.utils import load_yaml, build_yaml_path


class Query:
    """Object that connects to the json file"""

    def __init__(self, stats_type, **kwargs) -> None:
        self.stats_type = stats_type
        self.tags = kwargs

        yaml = load_yaml(build_yaml_path(f"{stats_type}.yaml"))
        self.headers, self.tag_dict = yaml['headers'], yaml['tags']
        self.validate_tags()
        self.set_tags()

        self.url = f"https://stats.nba.com/stats/leaguedash{stats_type}stats?" + "&".join(
            [f"{key}={value}" for key, value in self.tag_dict.items()]
        )

    def validate_tags(self):
        for tag in self.tags:
            if tag not in self.tag_dict:
                raise ValueError(f"{tag} is not a valid tag for {self.stats_type} stats")

    def set_tags(self):
        for tag in self.tags:
            self.tag_dict[tag] = f"{self.tags[tag]}"

    def json(self):
        return requests.get(self.url, headers=self.headers).json()

    def dataframe(self):
        response = self.json()["resultSets"][0]
        rows = response["rowSet"]
        col_names = response["headers"]
        return pd.DataFrame(rows, columns=col_names)