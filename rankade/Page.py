# Page.py

import rankade.Player
import rankade.ResultList


class Page(rankade.ResultList.ResultList):

    def _set_attributes(self, attributes):
        self.page = attributes.get("page")
        self.totalPages = attributes.get("totalPages")
        self.rowsForPage = attributes.get("rowsForPage")
        self.content = list()
        for data in attributes.get("data"):
            self.content.append(self._content_class(self._api, data))

    # To use the subclass must have an endpoint property.
    # Not content_class as that will return Match instead of Matches!

    async def next_page(self):
        if self.page >= self.totalPages:
            return None
        endpoint = "{}/{}".format(self.endpoint, self.page + 1)  # type: ignore
        
        return self.__class__(self._api, await self._api.get(endpoint))
