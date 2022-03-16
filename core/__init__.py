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
        if now.month == 1:
            mes = 'janeiro'
        elif now.month == 2:
            mes = 'fevereiro'
        elif now.month == 3:
            mes = 'março'
        elif now.month == 4:
            mes = 'abril'
        elif now.month == 5:
            mes = 'maio'
        elif now.month == 6:
            mes = 'junho'
        elif now.month == 7:
            mes = 'julho'
        elif now.month == 8:
            mes = 'agosto'  
        elif now.month == 9:
            mes = 'setembro' 
        elif now.month == 10:
            mes = 'outubro' 
        elif now.month == 11:
            mes = 'novembro' 
        elif now.month == 12:
            mes = 'dezembro'                       
        answer = f'Hoje é dia {now.day} de {mes} de {now.year}.'
        return answer