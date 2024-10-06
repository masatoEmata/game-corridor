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
        # 移動方向のベクトルを定義
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        if direction not in directions:
            return "無効な方向です。'up', 'down', 'left', 'right' のいずれかを入力してください。"
        delta_row, delta_col = directions[direction]
        new_row = self.soldier_position[0] + delta_row
        new_col = self.soldier_position[1] + delta_col

        # 勝利条件のチェック（右端を超えた場合）
        if new_col > self.field_width - 1:
            self.game_won = True
            return "ゲームに勝利しました！"
        # マップの範囲外への移動をチェック
        if (
            new_row < 0
            or new_row >= self.field_height
            or new_col < 0
            or new_col >= self.field_width
        ):
            return "エラー：マップの領域を超えています。"
        # ソルジャーの位置を更新
        self.map_x[self.soldier_position[0]][
            self.soldier_position[1]
        ] = 0  # 現在の位置をクリア
        self.soldier_position = [new_row, new_col]
        self.map_x[new_row][new_col] = 1  # 新しい位置にソルジャーを配置
        return f"ソルジャーは位置 {self.soldier_position} に移動しました。"
