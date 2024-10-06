import config


class Game:
    def __init__(self):
        # フィールドの初期化
        self.field_width = config.FIELD_WIDTH
        self.field_height = config.FIELD_HEIGHT
        self.map_x = [
            [0 for _ in range(self.field_width)] for _ in range(self.field_height)
        ]
        # ソルジャーの初期位置
        self.soldier_position = [1, 0]  # map_x[1][0]
        self.game_won = False
        # ソルジャーをフィールドに配置
        self.map_x[self.soldier_position[0]][
            self.soldier_position[1]
        ] = 1  # 1はソルジャーを表す

    def reset_game(self):
        self.__init__()

    def move_soldier(self, direction):
        if self.game_won:
            return "ゲームは既に終了しています。"
        if direction.lower() != "right":
            return "アラート：右にのみ移動できます。"
        else:
            # 現在の位置からソルジャーを削除
            self.map_x[self.soldier_position[0]][self.soldier_position[1]] = 0
            # 右に移動
            self.soldier_position[1] += 1
            if self.soldier_position[1] > self.field_width - 1:
                # フィールドを超えた場合
                self.game_won = True
                return "ゲームに勝利しました！"
            else:
                # 新しい位置にソルジャーを配置
                self.map_x[self.soldier_position[0]][self.soldier_position[1]] = 1
                return f"ソルジャーは位置{self.soldier_position}に移動しました。"
