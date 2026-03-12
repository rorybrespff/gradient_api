"""
Gradient API Package

This package provides functions for interacting with the Gradient Sports API,
including authentication, game data retrieval, and event processing.
"""

from .functions import (
    load_api_token,
    get_game_list,
    get_gameEvents_for_game,
    get_gameEvents_for_game_list,
)

__all__ = [
    "load_api_token",
    "get_game_list", 
    "get_gameEvents_for_game",
    "get_gameEvents_for_game_list",
]