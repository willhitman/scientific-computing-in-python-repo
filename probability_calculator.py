import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **balls):
        if len(balls)< 1:
            raise TypeError(
                f"'Hat' object takes at least 1 ball  positional arguments but {len(args)} were given"
            )
        self.contents = []
        for colour, count in balls.items():
            self.contents.extend([colour] *count)

    def __str__(self):
        hat =', '.join(self.contents)
        return hat
    
    def draw(self,number_of_balls):
        balls_picked = []
        if number_of_balls > len(self.contents):
            balls_picked = self.contents[:]
            self.contents.clear()
        else:
            balls_picked = random.sample(self.contents,
            number_of_balls) 

            for r in balls_picked:
                self.contents.remove(r)
        return balls_picked
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success_count = 0

    for _ in range(num_experiments):
        
        _hat = Hat(**Counter(hat.contents))

        drawn_balls = _hat.draw(num_balls_drawn)
        drawn_count = Counter(drawn_balls)

        success = all(drawn_count[color] >= count for color, count in expected_balls.items())
        if success:
            success_count += 1

    return success_count / num_experiments

hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=14,
                  num_experiments=2000)
