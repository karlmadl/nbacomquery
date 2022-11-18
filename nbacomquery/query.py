import requests
import pandas as pd
from nbacomquery.utils import load_yaml, build_yaml_path


class Query:
    """
    Uses `stats_type` and kwargs to build and execute a query string
    to nba.com/stats/. The `.json` method returns the raw query
    response. The `.dataframe` method parses json and returns pandas
    dataframe
    """

    def __init__(self, stats_type: str, **kwargs) -> None:
        self.stats_type = stats_type
        self.tags = kwargs

        yaml = load_yaml(build_yaml_path(f"{stats_type}.yaml"))
        self.headers, self.tag_dict = yaml["headers"], yaml["tags"]
        self.validate_tags()
        self.set_tags()

        self.url = f"https://stats.nba.com/stats/{yaml['url']}?" + "&".join(
            [f"{key}={value}" for key, value in self.tag_dict.items()]
        )

    def validate_tags(self) -> None:
        """
        Checks that all kwargs at class instantiation are valid query
        parameters/tags.
        """
        for tag in self.tags:
            if tag not in self.tag_dict:
                raise ValueError(
                    f"{tag} is not a valid tag for {self.stats_type} stats"
                )

    def set_tags(self) -> None:
        """
        Replaces all default query parameters that were specified by
        kwargs.
        """
        for tag in self.tags:
            self.tag_dict[tag] = f"{self.tags[tag]}"

    def json(self) -> dict:
        """
        Returns raw JSON response from query.
        """
        return requests.get(self.url, headers=self.headers).json()

    def dataframe(self):
        """
        Parses JSON reponse and returns pandas DataFrame.
        """
        response = self.json()["resultSets"][0]
        rows = response["rowSet"]
        col_names = response["headers"]
        return pd.DataFrame(rows, columns=col_names)
