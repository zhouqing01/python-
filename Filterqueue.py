import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, *args):
        super().__init__(*args)
        self.window = None

    def __contains__(self, filt):
        for i in self._queue:
            if filt(i):
                return True
        return False

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        else:
            self.put_nowait(self.get_nowait())
            if not self.empty():
                self.window = self._queue[0]  
            else:
                self.window = None

    async def put(self, val):
        if self.empty():
            self.window = val
        await super().put(val)


    async def get(self, filt=lambda x: True):
        if filt in self:
            for i in range(self.qsize()):
                el = await super().get()
                if filt(el):
                    if not self.empty():
                        self.window = self._queue[0] 
                    else:
                        self.window =None
                    return el
                await super().put(el)
        else:
            if not self.empty():
                self.window = self._queue[0]
            else:
                self.window = None
            return await super().get()