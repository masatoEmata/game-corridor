from fastapi import Depends, FastAPI
from pydantic import BaseModel

from game_logic import Game

app = FastAPI()


# ゲームインスタンスをシングルトンとして管理するクラス
class GameInstance:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = Game()
        return cls._instance


# 依存性の注入を使用してゲームインスタンスを取得
def get_game():
    return GameInstance.instance()


class MoveInput(BaseModel):
    direction: str


@app.get("/start")
def start_game(game: Game = Depends(get_game)):
    game.reset_game()
    return {
        "message": "ゲームが開始されました。",
        "soldier_position": game.soldier_position,
        "map_x": game.map_x,
    }


@app.post("/move")
def move_soldier(move_input: MoveInput, game: Game = Depends(get_game)):
    result = game.move_soldier(move_input.direction)
    return {
        "message": result,
        "soldier_position": game.soldier_position,
        "map_x": game.map_x,
    }
