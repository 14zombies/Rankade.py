# ResultList.py

import rankade.RankadeObject


class ResultList(rankade.RankadeObject.RankadeObject):

    def __init__(self, api, content_class, attributes):
        self._content_class = content_class
        super().__init__(api, attributes)

    def _set_attributes(self, attributes):
        self.content = list()
        if isinstance(attributes, list):
            for data in attributes:
                if data is not None:
                    self.content.append(self._content_class(self._api, data))
        elif isinstance(attributes, dict):
            data = attributes.get("data")
            if data is not None:
                self.content.append(self._content_class(self._api, data))
