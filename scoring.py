from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode='r') as high_score:
            prev_high_score = high_score.read()
            self.highscore = int(prev_high_score)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", False, align=ALIGNMENT, font=FONT)

    def reset_snake(self):
        if self.score > self.highscore:
            self.highscore = self.score
            high_score_file = self.highscore
            with open("high_score.txt", mode='w') as high_score:
                high_score.write(f"{high_score_file}")
        self.score = 0
        self.score_board()

    def scoring(self):
        self.score += 1
        self.score_board()
