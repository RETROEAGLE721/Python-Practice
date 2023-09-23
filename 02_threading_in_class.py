from collections.abc import Callable, Iterable, Mapping
from threading import Thread
import time
from typing import Any

start_time = time.time()
class cars(Thread):
    
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None , color) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.color = color
    
    def run(self):
        print(self.color)

class bike(Thread):

    def __init__(self,color, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.color = color
        
        
    def run(self):
        print(self.color)
        
        
car = cars(color="Red",daemon=True)
bike = bike(color="Black",daemon=True)
car.start()
print("This is your car")
bike.start()
print(time.time() - start_time)