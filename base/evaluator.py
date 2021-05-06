class Evaluator:
    def __init__(self, points):
        self.points = points
        self.stages = []
        self.correct_stages = []
        self.fines = []
        self.extra_fines = []
    
    @property
    def score(self):
        pass

    def evaluate(self, stages, res):
        for i in range(len(stages)):
            if stages[i] != self.correct_stages[i]:
                res -= self.fines[i]
                
                if self.extra_fines[i] > 0 and sum(x != y for x, y in zip(stages[i], self.correct_stages[i])) > 1:
                    res -= self.extra_fines[i]
        
        return res