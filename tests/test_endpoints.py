import unittest

from rankade.api.Endpoint import Endpoint, Endpoint_Request


class TestEndpoints(unittest.TestCase):
    def test_endpoints(self):
        auth = Endpoint_Request(Endpoint.AUTH)
        auth.add_parameter("parameter_key", "paramvalue")
        auth.add_header("header_key", "header_value")
        auth.set_json({"json_key": "json_value"})
        auth.page = 1

        self.assertEqual(auth.path, "auth")
        self.assertEqual(auth.method, "GET")
        self.assertFalse(auth.is_paginated)
        self.assertFalse(auth.requires_auth)
        self.assertEqual(auth.params["parameter_key"], "paramvalue")
        self.assertDictEqual(auth.headers, {"header_key": "header_value"})
        self.assertDictEqual(auth.json, {"json_key": "json_value"})
        self.assertEqual(auth.page, 1)

    def test_rankings_path(self):
        rankings = Endpoint_Request(Endpoint.RANKINGS)
        self.assertEqual(rankings.path, "rankings/last/1")
        rankings.subset = "9dYpN0xVeR3"
        self.assertEqual(rankings.subset, "9dYpN0xVeR3")
        rankings.match = 12
        self.assertEqual(rankings.match, 12)
        rankings.page = 2
        self.assertEqual(rankings.page, 2)
        self.assertEqual(rankings.path, "rankings/9dYpN0xVeR3/12/2")

    def test_matches_path(self):
        matches = Endpoint_Request(Endpoint.MATCHES)
        self.assertEqual(matches.path, "matches/1")
        matches.subset = "9dYpN0xVeR3"
        matches.page = 10
        self.assertEqual(matches.path, "matches/9dYpN0xVeR3/10")

    def test_players_path(self):
        players = Endpoint_Request(Endpoint.PLAYERS)
        self.assertEqual(players.path, "players/1")
        players.page = 3
        self.assertEqual(players.path, "players/3")


if __name__ == "__main__":
    unittest.main()
