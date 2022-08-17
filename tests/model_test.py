
import json
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

import rankade
from rankade.api.RankadeResponse import RankadeResponse
from rankade import models


def main():
    errors_str = r"""{
        "errors": [{
            "code": "A002",
            "message": "Authentication required"
        }]
    }"""
    errors_response = RankadeResponse(**json.loads(errors_str)).errors
    a_errors = models.Errors(
        None, "http://www.abc.com", "Get", 200, errors_response)
    errors_multi_str = r"""{
        "errors": [{
            "code": "A002",
            "message": "Authentication required"
        },{
            "code": "A003",
            "message": "Authentication required #2"
        }]
    }"""
    errors_multi_response = RankadeResponse(
        **json.loads(errors_multi_str)).errors
    a_errors_multi = models.Errors(
        None, "http://www.abc.com", "Get", 200, errors_multi_response)

    quota_str = r"""{
        "success": {
            "callsPerYear": "2%",
            "callsPerHour": "12%",
            "matchesPerYear": "3%",
            "matchesPerDay": "15%",
            "matchesPerHour": "0%",
            "rankingCallsPerYear": "2%",
            "rankingCallsPerDay": "5%",
            "rankingCallsPerHour": "10%",
            "apiCreatedGames": "1%"
        }
    }"""
    quota_response = RankadeResponse(**json.loads(quota_str)).success
    a_quota = models.Quota(None, **quota_response)

    token_str = r"""{
        "success": {
            "token": "jwt-token-here"
        }
    }"""
    token_response = RankadeResponse(**json.loads(token_str)).success
    a_token = models.Token(**token_response)

    players_str = r"""{
        "success": {
            "page": "2",
            "totalPages": 2,
            "rowsForPage": 25,
            "totalPlayers": 29,
            "data": [{
                    "id": "37VjKRy1a6p",
                    "ghost": 0,
                    "username": "Mackmansoup4585",
                    "displayName": "Mackmansoup",
                    "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
                },
                {
                    "id": "zqRjGDw4gbJ",
                    "ghost": 1,
                    "username": "",
                    "displayName": "*Emmephisto",
                    "icon": ""
                },
                {
                    "id": "Dwog3w8mgAL",
                    "ghost": 1,
                    "username": "",
                    "displayName": "*LongJohn",
                    "icon": ""
                },
                {
                    "id": "JVk1OklO1ov",
                    "ghost": 1,
                    "username": "",
                    "displayName": "*Captain Nemo",
                    "icon": ""
                }
            ]
        }
    }"""
    players_response = RankadeResponse(**json.loads(players_str)).success
    a_players = models.Players(None, **players_response)

    games_str = r"""{
        "success": [{
                "id": 962,
                "name": "Twilight Imperium (Third Edition)",
                "weight": "normal",
                "weightLabel": "Normal",
                "thumbnail": "https://cf.geekdo-images.com/thumb/img/fED6XRJVDYYOppNNmRfuU1vJr8Q=/fit-in/200x150/pic4128153.jpg",
                "mediumImage": "https://userscontents.rankade.com/images/500/4bdae1da8be6ecb837d0f8567ddb100e.jpg",
                "bggIdGame": 12493
            },
            {
                "id": 4579,
                "name": "Twilight Imperium: Fourth Edition",
                "weight": "normal",
                "weightLabel": "Normal",
                "thumbnail": "https://cf.geekdo-images.com/thumb/img/UOV5jJadzHc6ebYd5CfZXGbOWsc=/fit-in/200x150/pic3727516.jpg",
                "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/956d6ab81f37aef3db55d5909cf92ab8.jpg",
                "bggIdGame": 233078
            },
            {
                "id": 4784,
                "name": "Twilight Squabble",
                "weight": "normal",
                "weightLabel": "Normal",
                "thumbnail": "https://cf.geekdo-images.com/thumb/img/BOsJzM6uF6GdjaGd8i45xvQ_16U=/fit-in/200x150/pic2908587.png",
                "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/3f00c90fea5f03698038df48c584e799.png",
                "bggIdGame": 191364
            },
            {
                "id": 963,
                "name": "Twilight Struggle",
                "weight": "normal",
                "weightLabel": "Normal",
                "thumbnail": "https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg",
                "mediumImage": "https://userscontents.rankade.com/images/500/6f2f6d3c4ec73f443527a808a62b0261.jpg",
                "bggIdGame": 12333
            }
        ]
    }"""
    games_response = RankadeResponse(**json.loads(games_str)).success
    a_games = models.Games(None, games_response)

    matches_str = r"""{
        "success": {
            "page": 2,
            "totalPages": 2,
            "rowsForPage": 25,
            "totalMatches": 28,
            "data": [{
                    "id": "Jowlqr5o0qA",
                    "externalId": "",
                    "date": "2019-12-20 10:45:00",
                    "registrationDate": "2019-12-20 10:46:01",
                    "number": 3,
                    "summary": "Captain Nemo\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 16,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                },
                {
                    "id": "kMAxQ8GRYOq",
                    "externalId": "",
                    "date": "2019-12-20 10:19:34",
                    "registrationDate": "2019-12-20 10:20:12",
                    "number": 2,
                    "summary": "MackmanSoup\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 9,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": "Weather was fine"
                },
                {
                    "id": "kRplW5vnYqE",
                    "externalId": "",
                    "date": "2019-12-20 09:34:54",
                    "registrationDate": "2019-12-20 09:35:32",
                    "number": 1,
                    "summary": "Emmephisto\nMackmanSoup",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "zqRjGDw4gbJ",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Emmephisto",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 19,
                            "players": [{
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                }
            ]
        }
    }"""
    matches_response = RankadeResponse(**json.loads(matches_str)).success
    a_matches = models.Matches(None, **matches_response)

    matches_status_str = r"""{
        "success": {
            "queued": 0,
            "waiting": 0,
            "added": 83,
            "processed": 83,
            "total": 83
        }
    }"""
    matches_status_response = RankadeResponse(
        **json.loads(matches_status_str)).success
    a_matches_status = models.MatchStatus(
        None, **matches_status_response)

    match_post_str = r"""{
        "success": {
            "total": 2,
            "accepted": [{
                "index": 0,
                "id": "wweq",
                "name": null,
                "errors": []
            }],
            "acceptedCount": 1,
            "rejected": [{
                "index": 1,
                "id": "312",
                "name": null,
                "errors": [{
                    "code": "M003",
                    "message": "A match with the same external identifier was already accepted"
                }]
            }],
            "rejectedCount": 1
        }
    }"""
    match_post_response = RankadeResponse(**json.loads(match_post_str)).success
    a_match_post = models.NewMatchResponse(None, **match_post_response)

    subsets_str = r"""{
        "success": [{
                "id": "oBypZD7Vngx",
                "name": "Main",
                "type": "main",
                "creationDate": "2019-12-20 09:23:48",
                "isMain": 1,
                "isCustom": 0,
                "icon": "https://userscontents.rankade.com/images/256/game_icon_placeholder.png",
                "game": null,
                "countMatches": 47,
                "firstMatch": {
                    "id": "kRplW5enYqE",
                    "externalId": "",
                    "date": "2019-12-20 09:25:28",
                    "registrationDate": "2019-12-20 09:25:48",
                    "number": 1,
                    "summary": "LongJohn\nCaptain Nemo",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 18,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                },
                "lastMatch": {
                    "id": "Jowlqr5o0qA",
                    "externalId": "",
                    "date": "2019-12-20 10:16:50",
                    "registrationDate": "2019-12-20 10:17:01",
                    "number": 47,
                    "summary": "Captain Nemo\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 12,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                }
            },
            {
                "id": "PDyKv5gpG2R",
                "name": "Table Football",
                "type": "game",
                "creationDate": "2019-12-20 10:17:06",
                "isMain": 0,
                "isCustom": 0,
                "icon": "https://cf.geekdo-images.com/images/pic1107292_t.jpg",
                "game": {
                    "id": 1335,
                    "name": "Table Football",
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "thumbnail": "https://cf.geekdo-images.com/images/pic1107292_t.jpg",
                    "mediumImage": "",
                    "bggIdGame": null
                },
                "countMatches": 22,
                "firstMatch": {
                    "id": "rKb0Mpe8leE",
                    "externalId": "",
                    "date": "2019-12-20 09:28:03",
                    "registrationDate": "2019-12-20 09:28:20",
                    "number": 1,
                    "summary": "Captain Nemo\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1335,
                        "name": "Table Football",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://cf.geekdo-images.com/images/pic1107292_t.jpg",
                        "mediumImage": "",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 11,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 7,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                },
                "lastMatch": {
                    "id": "B3VxkNpkYoZ",
                    "externalId": "",
                    "date": "2019-12-20 10:14:31",
                    "registrationDate": "2019-12-20 10:14:42",
                    "number": 22,
                    "summary": "MackmanSoup\nCaptain Nemo",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1335,
                        "name": "Table Football",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://cf.geekdo-images.com/images/pic1107292_t.jpg",
                        "mediumImage": "",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 11,
                            "players": [{
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 9,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                }
            },
            {
                "id": "0lvKeQgKwRr",
                "name": "Table Tennis",
                "type": "game",
                "creationDate": "2019-12-20 10:17:12",
                "isMain": 0,
                "isCustom": 0,
                "icon": "https://cf.geekdo-images.com/images/pic1107292_t.jpg",
                "game": {
                    "id": 1334,
                    "name": "Table Tennis",
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                    "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                    "bggIdGame": null
                },
                "countMatches": 25,
                "firstMatch": {
                    "id": "kRplW5enYqE",
                    "externalId": "",
                    "date": "2019-12-20 09:25:28",
                    "registrationDate": "2019-12-20 09:25:48",
                    "number": 1,
                    "summary": "LongJohn\nCaptain Nemo",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 18,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                },
                "lastMatch": {
                    "id": "Jowlqr5o0qA",
                    "externalId": "",
                    "date": "2019-12-20 10:16:50",
                    "registrationDate": "2019-12-20 10:17:01",
                    "number": 25,
                    "summary": "Captain Nemo\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 12,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                }
            }
        ]
    }"""
    subsets_response = RankadeResponse(**json.loads(subsets_str)).success
    a_subsets = models.Subsets(None, subsets_response)

    rankings_str = r"""{
        "success": {
            "page": 2,
            "totalPages": 2,
            "rowsForPage": 25,
            "data": [{
                    "player": {
                        "id": "zqRjGDw4gbJ",
                        "ghost": 1,
                        "username": "",
                        "displayName": "*Emmephisto",
                        "icon": ""
                    },
                    "ree": 2043,
                    "deltaRee": -2,
                    "position": 26,
                    "deltaPosition": 0,
                    "belt": 0,
                    "beltLabel": "",
                    "title": 4,
                    "titleLabel": "",
                    "status": 3,
                    "statusLabel": "active"
                },
                {
                    "player": {
                        "id": "37VjKRy1a6p",
                        "ghost": 0,
                        "username": "Mackmansoup4585",
                        "displayName": "Mackmansoup",
                        "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
                    },
                    "ree": 1981,
                    "deltaRee": 0,
                    "position": 27,
                    "deltaPosition": 1,
                    "belt": 0,
                    "beltLabel": "",
                    "title": 0,
                    "titleLabel": "",
                    "status": 3,
                    "statusLabel": "active"
                },
                {
                    "player": {
                        "id": "JVk1OklO1ov",
                        "ghost": 1,
                        "username": "",
                        "displayName": "*Captain Nemo",
                        "icon": ""
                    },
                    "ree": 1974,
                    "deltaRee": 10,
                    "position": 28,
                    "deltaPosition": 2,
                    "belt": 0,
                    "beltLabel": "",
                    "title": 0,
                    "titleLabel": "",
                    "status": 3,
                    "statusLabel": "active"
                },
                {
                    "player": {
                        "id": "Dwog3w8mgAL",
                        "ghost": 1,
                        "username": "",
                        "displayName": "*LongJohn",
                        "icon": ""
                    },
                    "ree": 1900,
                    "deltaRee": -9,
                    "position": 29,
                    "deltaPosition": -1,
                    "belt": 0,
                    "beltLabel": "",
                    "title": 0,
                    "titleLabel": "",
                    "status": 3,
                    "statusLabel": "active"
                }
            ],
            "subset": {
                "id": "oBypZD7Vngx",
                "name": "Main",
                "type": "main",
                "creationDate": "2019-12-20 09:23:48",
                "isMain": 1,
                "isCustom": 0,
                "icon": "https://userscontents.rankade.com/images/256/game_icon_placeholder.png",
                "game": null,
                "countMatches": 47,
                "firstMatch": {
                    "id": "kRplW5enYqE",
                    "externalId": "",
                    "date": "2019-12-20 09:25:28",
                    "registrationDate": "2019-12-20 09:25:48",
                    "number": 1,
                    "summary": "LongJohn\nCaptain Nemo",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 18,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                },
                "lastMatch": {
                    "id": "Jowlqr5o0qA",
                    "externalId": "",
                    "date": "2019-12-20 10:16:50",
                    "registrationDate": "2019-12-20 10:17:01",
                    "number": 47,
                    "summary": "Captain Nemo\nLongJohn",
                    "type": "player_vs_player",
                    "draw": 0,
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "game": {
                        "id": 1334,
                        "name": "Table Tennis",
                        "weight": "normal",
                        "weightLabel": "Normal",
                        "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                        "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                        "bggIdGame": null
                    },
                    "factions": [{
                            "rank": 1,
                            "name": "",
                            "points": 21,
                            "players": [{
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 1,
                            "bot": 0
                        },
                        {
                            "rank": 2,
                            "name": "",
                            "points": 12,
                            "players": [{
                                "id": "Dwog3w8mgAL",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*LongJohn",
                                "icon": ""
                            }],
                            "countPlayers": 1,
                            "winner": 0,
                            "bot": 0
                        }
                    ],
                    "notes": ""
                }
            },
            "match": {
                "id": "Jowlqr5o0qA",
                "externalId": "",
                "date": "2019-12-20 10:16:50",
                "registrationDate": "2019-12-20 10:17:01",
                "number": 47,
                "summary": "Captain Nemo\nLongJohn",
                "type": "player_vs_player",
                "draw": 0,
                "weight": "normal",
                "weightLabel": "Normal",
                "game": {
                    "id": 1334,
                    "name": "Table Tennis",
                    "weight": "normal",
                    "weightLabel": "Normal",
                    "thumbnail": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
                    "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
                    "bggIdGame": null
                },
                "factions": [{
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [{
                            "id": "JVk1OklO1ov",
                            "ghost": 1,
                            "username": "",
                            "displayName": "*Captain Nemo",
                            "icon": ""
                        }],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 12,
                        "players": [{
                            "id": "Dwog3w8mgAL",
                            "ghost": 1,
                            "username": "",
                            "displayName": "*LongJohn",
                            "icon": ""
                        }],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0
                    }
                ],
                "notes": ""
            }
        }
    }"""
    rankings_response = RankadeResponse(**json.loads(rankings_str)).success
    a_rankings = models.Rankings(None, **rankings_response)
    a111 = models.Games(None, None)
    print("foo")


if __name__ == "__main__":
    main()
