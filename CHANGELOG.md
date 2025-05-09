## v0.1.6
- Added: dryrun parameter to NewMatchResponse.
- Fixed: Drone signing.

## v0.1.5
- Fixed: Test TestRankadePlayers.test_get_all_players
- Fixed: Rankade.get_all_players now returns actual Player's in the Players object.

## v0.1.4
- Fixed: Issue with session being closed, but not None in rankade.Api.

## v0.1.2
- Updated: enum_tools added to dependencies.
- Updated: .drone.yml to fix minor build issues.

## v0.1.1
- Fixed: setup.py repair.
- Fixed: rankade.consts/rankade.Consts mix-up.

## v0.1.0
- Added: Type hints to all the things.
- Added: TypeAliases for JSON (JSON), HTTP Parameters (PARAMS), & HTTP Headers (HEADERS).
- Added: Endpoint_Method, Endpoint_Mixin, & Endpoint_Request as using the Endpoint enum for all request info was causing issues.
- Added: NewMatch type and Api.save method.
- Added: Support for dry_run in Api.save method.
- Added: Makefile to simplify running tests/building docs/etc"
- Added: examples for documentation.
- Moved: Token back to Api Submodule.
- Removed: Api from all RankadeObjects.
- Removed: setup.cfg & setup.py.
- Updated: Moved all magic strings to consts.py.
- Updated: RankadeClass renamed to Rankade.
- Updated: Finished all documentation.
- Updated: API is now a context manager.
- Updated: Refactored Api._request to deal with errors in a cleaner manner.
- Updated: Base classes to use Generics.
- Updated: README.md for v0.1.0.
- Updated: Removed requirements.txt as moved to pyproject.toml.
- Updated: Moved to pyproject.toml.
- Updated: Tests for v0.1.0.
- Updated: .gitignore.
- Updated: Documentation for v0.1.0.

## v0.0.2
- Fixed: Player IDs read in Faction.to_json() instead of player object
