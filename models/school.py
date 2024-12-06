class School:
    def __init__(self, name = "", preferences= [], capacity = 0):
        self.name = name
        self.preferences = preferences
        self.capacity = capacity
        self.current_matches = []

    def prefers(self, student1, student2):
        """2人の生徒を比較し、どちらを優先するかを返す"""
        return self.preferences.index(student1.name) < self.preferences.index(student2.name)

    def accept_proposal(self, student):
        """提案を受け入れるかどうかを決定し、現在のマッチを更新する"""
        self.current_matches.append(student)
        self.current_matches.sort(key=lambda s: self.preferences.index(s.name))
        if len(self.current_matches) > self.capacity:
            rejected_student = self.current_matches.pop()
            return rejected_student
        return None
    
    def give_seat(self, student):
        """空きがある場合に生徒に席を渡す"""
        if len(self.current_matches) < self.capacity:
            self.current_matches.append(student)
            return True
        return False
    
    def __repr__(self):
        return f"School({self.name})"