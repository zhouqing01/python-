import asyncio


class NotifyEvent(asyncio.Event):
    def __init__(self):
        super().__init__()

    def set(self, name=None):
        self.name = name
        super().set()

    async def wait(self):
        await super().wait()
        super().clear()
        return self.name

def compare(name1,name):
    if name1 == name:
        return 1
    else:
        return 0

async def task(name, event, d={}):
    while True:
        name1 = await event.wait()
        if name1:
            if compare(name1,name) == 1:
                d[name] = d.get(name, 0) +  1
                kol = sum(d.values())
                print(f'{name}: {d[name]} / {kol - d[name]}')
        else:
            break
