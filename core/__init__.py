import datetime

class SystemInfo:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos.'
        return answer
    
    @staticmethod
    def get_day():
        now = datetime.datetime.now()
        if now.month == 3:
            mes = 'março'
        answer = f'Hoje é dia {now.day} de {mes} de {now.year}.'
        return answer