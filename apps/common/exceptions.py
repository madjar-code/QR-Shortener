class InvalidFormat(Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self) -> str:
        if self.message:
            return f'Недопустимый формат: {self.message}!'
        else:
            return 'Какой-то недопустимый формат!'