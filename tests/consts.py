import datetime
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt

null = None
base_url = "https://api.rankade.com/public/api/1/"


game = {
    "id": 962,
    "name": "Twilight Imperium (Third Edition)",
    "weight": "normal",
    "weightLabel": "Normal",
    "thumbnail": "https://cf.geekdo-images.com/thumb/img/fED6XRJVDYYOppNNmRfuU1vJr8Q=/fit-in/200x150/pic4128153.jpg",
    "mediumImage": "https://userscontents.rankade.com/images/500/4bdae1da8be6ecb837d0f8567ddb100e.jpg",
    "bggIdGame": 12493,
}

faction_dict = {"rank": 1, "score": "21", "players": ["Dwog3w8mgAL"]}

factions_dict = {
    "data": [
        {
            "rank": 1,
            "name": "",
            "points": 21,
            "players": [{"id": "JVk1OklO1ov", "ghost": 1, "username": "", "displayName": "*Captain Nemo", "icon": ""}],
            "countPlayers": 1,
            "winner": 1,
            "bot": 0,
        },
        {
            "rank": 2,
            "name": "",
            "points": 16,
            "players": [{"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}],
            "countPlayers": 1,
            "winner": 0,
            "bot": 0,
        },
    ],
}

match_postvalue = [
    {
        "game": 1334,
        "weight": "normal",
        "factions": [
            {"rank": 1, "score": "21", "players": ["JVk1OklO1ov"]},
            {"rank": 2, "score": "16", "players": ["Dwog3w8mgAL"]},
        ],
        "notes": "",
    }
]

notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


#######################
#       TOKENS        #
#######################


valid_token_message = {
    "iat": (datetime.now(timezone.utc)),
    "exp": (datetime.now(timezone.utc) + timedelta(hours=1)),
}

invalid_token_message = {
    "iat": (datetime.now(timezone.utc) - timedelta(hours=2)),
    "exp": (datetime.now(timezone.utc) - timedelta(hours=1)),
}


def make_token(token: Dict[str, Any]) -> str:
    jwtoken = jwt.encode(token, key="", algorithm="HS256")
    return jwtoken


#######################
# MOCK SERVER RETURNS #
#######################

errors_returnvalue = {"errors": [{"code": "A002", "message": "Authentication required"}]}
errors_multi_returnvalue = {
    "errors": [
        {"code": "A002", "message": "Authentication required"},
        {"code": "A003", "message": "Authentication required #2"},
    ]
}
errors_match_validation_400_M001 = {"errors": [{"code": "M001", "message": "Invalid JSON message in request."}]}
errors_match_validation_202_M002 = {"errors": [{"code": "M002", "message": "JSON schema validation error."}]}
errors_match_validation_401_A001 = {"errors": [{"code": "A001", "message": "Invalid credentials or client disabled."}]}
errors_match_validation_429_Q001 = {
    "errors": [{"code": "Q001", "message": "API calls per year limit has been reached."}]
}
errors_match_validation_500_R001 = {"errors": [{"code": "R001", "message": "Generic error."}]}
games_returnvalue = {
    "success": [
        {
            "id": 962,
            "name": "Twilight Imperium (Third Edition)",
            "weight": "normal",
            "weightLabel": "Normal",
            "thumbnail": "https://cf.geekdo-images.com/thumb/img/fED6XRJVDYYOppNNmRfuU1vJr8Q=/fit-in/200x150/pic4128153.jpg",
            "mediumImage": "https://userscontents.rankade.com/images/500/4bdae1da8be6ecb837d0f8567ddb100e.jpg",
            "bggIdGame": 12493,
        },
        {
            "id": 4579,
            "name": "Twilight Imperium: Fourth Edition",
            "weight": "normal",
            "weightLabel": "Normal",
            "thumbnail": "https://cf.geekdo-images.com/thumb/img/UOV5jJadzHc6ebYd5CfZXGbOWsc=/fit-in/200x150/pic3727516.jpg",
            "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/956d6ab81f37aef3db55d5909cf92ab8.jpg",
            "bggIdGame": 233078,
        },
        {
            "id": 4784,
            "name": "Twilight Squabble",
            "weight": "normal",
            "weightLabel": "Normal",
            "thumbnail": "https://cf.geekdo-images.com/thumb/img/BOsJzM6uF6GdjaGd8i45xvQ_16U=/fit-in/200x150/pic2908587.png",
            "mediumImage": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/3f00c90fea5f03698038df48c584e799.png",
            "bggIdGame": 191364,
        },
        {
            "id": 963,
            "name": "Twilight Struggle",
            "weight": "normal",
            "weightLabel": "Normal",
            "thumbnail": "https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg",
            "mediumImage": "https://userscontents.rankade.com/images/500/6f2f6d3c4ec73f443527a808a62b0261.jpg",
            "bggIdGame": 12333,
        },
    ]
}
new_game_returnvalue = {
    "success": [
        {
            "id": 963,
            "name": "Twilight Struggle",
            "weight": "normal",
            "weightLabel": "Normal",
            "thumbnail": "https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg",
            "mediumImage": "https://userscontents.rankade.com/images/500/6f2f6d3c4ec73f443527a808a62b0261.jpg",
            "bggIdGame": 12333,
        }
    ]
}
matches_status_returnvalue = {"success": {"queued": 0, "waiting": 0, "added": 83, "processed": 83, "total": 83}}
matches_returnvalue_page_2 = {
    "success": {
        "page": 2,
        "totalPages": 2,
        "rowsForPage": 25,
        "totalMatches": 28,
        "data": [
            {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 16,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 9,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "Weather was fine",
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {"id": "zqRjGDw4gbJ", "ghost": 1, "username": "", "displayName": "*Emmephisto", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 19,
                        "players": [
                            {
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
        ],
    }
}
matches_returnvalue_page_1 = {
    "success": {
        "page": 1,
        "totalPages": 2,
        "rowsForPage": 25,
        "totalMatches": 28,
        "data": [
            {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 16,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 9,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "Weather was fine",
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {"id": "zqRjGDw4gbJ", "ghost": 1, "username": "", "displayName": "*Emmephisto", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 19,
                        "players": [
                            {
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
        ],
    }
}
match_returnvalue = {
    "success": {
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
            "bggIdGame": null,
        },
        "factions": [
            {
                "rank": 1,
                "name": "",
                "points": 21,
                "players": [
                    {
                        "id": "JVk1OklO1ov",
                        "ghost": 1,
                        "username": "",
                        "displayName": "*Captain Nemo",
                        "icon": "",
                    }
                ],
                "countPlayers": 1,
                "winner": 1,
                "bot": 0,
            },
            {
                "rank": 2,
                "name": "",
                "points": 16,
                "players": [{"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}],
                "countPlayers": 1,
                "winner": 0,
                "bot": 0,
            },
        ],
        "notes": "",
    },
}
match_post_returnvalue = {
    "success": {
        "total": 2,
        "accepted": [{"index": 0, "id": "wweq", "name": null, "errors": []}],
        "acceptedCount": 1,
        "rejected": [
            {
                "index": 1,
                "id": "312",
                "name": null,
                "errors": [
                    {"code": "M003", "message": "A match with the same external identifier was already accepted"}
                ],
            }
        ],
        "rejectedCount": 1,
    }
}
match_post_dict = {
    "data": [
        {
            "game": 962,
            "name": "",
            "weight": "normal",
            "factions": [
                {"rank": 1, "score": "21", "players": ["JVk1OklO1ov"]},
                {"rank": 2, "score": "16", "players": ["Dwog3w8mgAL"]},
            ],
            "notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        }
    ]
}
players_returnvalue = {
    "success": {
        "page": 1,
        "totalPages": 1,
        "rowsForPage": 25,
        "totalPlayers": 4,
        "data": [
            {
                "id": "37VjKRy1a6p",
                "ghost": 0,
                "username": "Mackmansoup4585",
                "displayName": "Mackmansoup",
                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
            },
            {"id": "zqRjGDw4gbJ", "ghost": 1, "username": "", "displayName": "*Emmephisto", "icon": ""},
            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""},
            {"id": "JVk1OklO1ov", "ghost": 1, "username": "", "displayName": "*Captain Nemo", "icon": ""},
        ],
    }
}
new_ghost_player_returnvalue = {
    "success": [{"id": "zqRjGDw4gbJ", "ghost": 1, "username": "", "displayName": "*Emmephisto", "icon": ""}]
}
quota_returnvalue = {
    "success": {
        "callsPerYear": "2%",
        "callsPerHour": "12%",
        "matchesPerYear": "3%",
        "matchesPerDay": "15%",
        "matchesPerHour": "0%",
        "rankingCallsPerYear": "2%",
        "rankingCallsPerDay": "5%",
        "rankingCallsPerHour": "10%",
        "apiCreatedGames": "1%",
    }
}
rankings_returnvalue = {
    "success": {
        "page": 1,
        "totalPages": 1,
        "rowsForPage": 25,
        "data": [
            {
                "player": {"id": "zqRjGDw4gbJ", "ghost": 1, "username": "", "displayName": "*Emmephisto", "icon": ""},
                "ree": 2043,
                "deltaRee": -2,
                "position": 26,
                "deltaPosition": 0,
                "belt": 0,
                "beltLabel": "",
                "title": 4,
                "titleLabel": "",
                "status": 3,
                "statusLabel": "active",
            },
            {
                "player": {
                    "id": "37VjKRy1a6p",
                    "ghost": 0,
                    "username": "Mackmansoup4585",
                    "displayName": "Mackmansoup",
                    "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
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
                "statusLabel": "active",
            },
            {
                "player": {"id": "JVk1OklO1ov", "ghost": 1, "username": "", "displayName": "*Captain Nemo", "icon": ""},
                "ree": 1974,
                "deltaRee": 10,
                "position": 28,
                "deltaPosition": 2,
                "belt": 0,
                "beltLabel": "",
                "title": 0,
                "titleLabel": "",
                "status": 3,
                "statusLabel": "active",
            },
            {
                "player": {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""},
                "ree": 1900,
                "deltaRee": -9,
                "position": 29,
                "deltaPosition": -1,
                "belt": 0,
                "beltLabel": "",
                "title": 0,
                "titleLabel": "",
                "status": 3,
                "statusLabel": "active",
            },
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 18,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
            "lastMatch": {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 16,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
        },
        "match": {
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
                "bggIdGame": null,
            },
            "factions": [
                {
                    "rank": 1,
                    "name": "",
                    "points": 21,
                    "players": [
                        {"id": "JVk1OklO1ov", "ghost": 1, "username": "", "displayName": "*Captain Nemo", "icon": ""}
                    ],
                    "countPlayers": 1,
                    "winner": 1,
                    "bot": 0,
                },
                {
                    "rank": 2,
                    "name": "",
                    "points": 16,
                    "players": [
                        {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                    ],
                    "countPlayers": 1,
                    "winner": 0,
                    "bot": 0,
                },
            ],
            "notes": "",
        },
    }
}
subsets_returnvalue = {
    "success": [
        {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 18,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
            "lastMatch": {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 16,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
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
                "bggIdGame": null,
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 11,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 7,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 11,
                        "players": [
                            {
                                "id": "37VjKRy1a6p",
                                "ghost": 0,
                                "username": "Mackmansoup4585",
                                "displayName": "Mackmansoup",
                                "icon": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 9,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
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
                "bggIdGame": null,
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 18,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
            "lastMatch": {
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
                    "bggIdGame": null,
                },
                "factions": [
                    {
                        "rank": 1,
                        "name": "",
                        "points": 21,
                        "players": [
                            {
                                "id": "JVk1OklO1ov",
                                "ghost": 1,
                                "username": "",
                                "displayName": "*Captain Nemo",
                                "icon": "",
                            }
                        ],
                        "countPlayers": 1,
                        "winner": 1,
                        "bot": 0,
                    },
                    {
                        "rank": 2,
                        "name": "",
                        "points": 16,
                        "players": [
                            {"id": "Dwog3w8mgAL", "ghost": 1, "username": "", "displayName": "*LongJohn", "icon": ""}
                        ],
                        "countPlayers": 1,
                        "winner": 0,
                        "bot": 0,
                    },
                ],
                "notes": "",
            },
        },
    ]
}

token_returnvalue = {"success": {"token": "jwt-token-here"}}
