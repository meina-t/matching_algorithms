class Student:
    def __init__(self, name = "", preferences = []):
        self.name = name
        self.preferences = preferences
        self.current_proposal_index = 0
        self.matched_school = None

    def propose(self) -> str:
        """断られていない学校があれば、その中で一番好きな学校（前のプロポーズより一つ後の学校）に提案する"""
        if self.current_proposal_index < len(self.preferences):
            school_name = self.preferences[self.current_proposal_index]
            self.current_proposal_index += 1
            return school_name
        return None

    def __repr__(self):
        return f"Student({self.name})"

