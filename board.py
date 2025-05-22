#6
class Whiteboard:
    def __init__(self, name="Доска", initial_messages=None):
        self.name = name
        self._messages = []
        
        if initial_messages is not None:
            if not isinstance(initial_messages, list):
                raise TypeError("Начальные сообщения должны быть списком")
            
            for msg in initial_messages:
                self.add_message(msg)
    
    def add_message(self, message):
        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")
        
        self._messages.append(message)
        return self  
    
    def clear(self):
        self._messages = []
        return self
    
    @property
    def latest_message(self):
        if not self._messages:
            return None
        return self._messages[-1]
    
    @latest_message.setter
    def latest_message(self, message):
        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")
        
        if not self._messages:
            raise ValueError("Невозможно изменить последнее сообщение: доска пуста")
        
        self._messages[-1] = message
    
    def __add__(self, other):
        if not isinstance(other, Whiteboard):
            raise TypeError("Можно объединять только с другой доской")
        
        combined_name = f"{self.name} + {other.name}"
        combined_messages = self._messages + other._messages
        return Whiteboard(combined_name, combined_messages)
    
    def __len__(self):
        return len(self._messages)
    
    def __call__(self):
        if not self._messages:
            return f"{self.name} (пусто)"
        
        header = f"{self.name} ({len(self)} сообщений):"
        messages = "\n".join([f"- {msg}" for msg in self._messages])
        return f"{header}\n{messages}"
    
    def __str__(self):
        return f"{self.name} ({len(self)} сообщений)"


