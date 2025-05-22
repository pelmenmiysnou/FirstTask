#3
class Student:
    def __init__(self, name, scores=None):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        
        self.name = name
        self.scores = [] if scores is None else self._validate_scores(scores)
    
    def _validate_scores(self, scores):
        if not isinstance(scores, list):
            raise TypeError("Оценки должны быть представлены в виде списка")
        
        validated_scores = []
        for score in scores:
            if not isinstance(score, (int, float)):
                raise TypeError("Оценки должны быть числами")
            if score < 0 or score > 100:
                raise ValueError("Оценки должны быть в диапазоне от 0 до 100")
            validated_scores.append(score)
        
        return validated_scores
    
    def add_score(self, score):
        self.scores.extend(self._validate_scores([score]))
    
    def get_grade(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод")
    
    def __str__(self):
        return f"Студент: {self.name}, Оценки: {self.scores}"


class MathStudent(Student):
    def get_grade(self):
        if not self.scores:
            return "Нет оценок"
        
        avg_score = sum(self.scores) / len(self.scores)
        
        if avg_score >= 90:
            return "A"
        elif avg_score >= 75:
            return "B"
        elif avg_score >= 60:
            return "C"
        else:
            return "D"
    
    def __str__(self):
        return f"Студент-математик: {self.name}, Оценки: {self.scores}, Итоговая оценка: {self.get_grade()}"


class HistoryStudent(Student):
    def get_grade(self):
        if not self.scores:
            return "Нет оценок"
        
        sorted_scores = sorted(self.scores)
        n = len(sorted_scores)
        
        if n % 2 == 0:
            median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2
        else:
            median = sorted_scores[n//2]
        
        if median >= 85:
            return "Отлично"
        elif median >= 70:
            return "Хорошо"
        elif median >= 50:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"
    
    def __str__(self):
        return f"Студент-историк: {self.name}, Оценки: {self.scores}, Итоговая оценка: {self.get_grade()}"
