import pytest
import allure

from core.player import Player
from core.analytics import GameAnalytics
from utils.logger import Logger


@pytest.fixture
def player():
    analytics = GameAnalytics()
    logger = Logger()
    return Player(analytics, logger), analytics, logger


@allure.feature("Player")
@allure.story("Coins")
def test_add_coins(player):
    player_obj, analytics, logger = player

    with allure.step("Добавляем 100 монет"):
        player_obj.add_coins(100)

    assert player_obj.coins == 100


@allure.feature("Player")
@allure.story("Coins")
def test_spend_coins_success(player):
    player_obj, analytics, logger = player

    player_obj.add_coins(100)

    with allure.step("Тратим 50 монет"):
        result = player_obj.spend_coins(50)

    assert result is True
    assert player_obj.coins == 50


@allure.feature("Player")
@allure.story("Analytics")
def test_analytics_event(player):
    player_obj, analytics, logger = player

    player_obj.add_coins(100)
    player_obj.spend_coins(50)

    assert "purchase_success" in analytics.events


@allure.feature("Player")
@allure.story("Logs")
def test_logs(player):
    player_obj, analytics, logger = player

    player_obj.add_coins(100)

    assert "Coins added: 100" in logger.logs