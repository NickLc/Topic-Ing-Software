
class Handler():
    """
    The Handler interfae declares a method for building the
    chain of handlers. It also declarate a method for executing a request
    """

    #@abstractmethod
    def set_next(self, handler):
        pass
    
    #@abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    """
    Ther default chaining behovior can be implement inside a base handler
    class.
    """
    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        
        return None

"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""
# request = number millas
# handle = calcule millas win

class HPlata(AbstractHandler):
    def handle(self, request):
        if request < 100:
            print("H_Plata Atendiendo Solicitud\n")
            win_millas = 60
            return  win_millas
        else:
            print("Pasando a H_Oro")
            return super().handle(request)

class HOro(AbstractHandler):
    def handle(self, request):
        if request < 200:
            print("H_Oro Atendiendo Solicitud")
            win_millas = 20
            return  win_millas
        else:
            return super().handle(request)

plata = HPlata()
oro = HOro()
plata.set_next(oro)

result = plata.handle(150)
print(result)