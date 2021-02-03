# RankadeObject.py

class RankadeObject(object):

    def __init__(self, api, attributes):
        self._api = api
        # Root returned from Rankade API is either a success or errors object,
        # once this is stripped out the child objects should just be passed
        # through.
        stripped_attributes = attributes.get("success")
        if stripped_attributes is None:
            stripped_attributes = attributes.get("errors")
        if stripped_attributes is None:
            stripped_attributes = attributes
        self._set_attributes(stripped_attributes)

    def _set_attributes(self, attributes):
        pass
