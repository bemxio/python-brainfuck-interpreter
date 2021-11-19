import debugger
import json
import sys

class Interpreter:
    def __init__(self, dialect="dialects/default.json", debugger=None, size=30000):
        self.array = [0 for _ in range(size)]
        self.pointer = 0
        self.size = size
        
        self.dialect = None
        self.load_dialect(dialect)
        
        self.debugger = debugger
    
    def load_dialect(self, dialect):
        with open(dialect, "r") as f:
            self.dialect = json.load(f)

    # functions for manipulating the pointer & array
    def right(self):
        self.pointer += 1
        if self.pointer > self.size - 1:
            self.pointer = 0
    
    def left(self):
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = self.size - 1
    
    def plus(self):
        self.array[self.pointer] += 1
        if self.array[self.pointer] > 255:
            self.array[self.pointer] = 0
    
    def minus(self):
        self.array[self.pointer] -= 1
        if self.array[self.pointer] < 0:
            self.array[self.pointer] = 255
            
    def input(self):
        self.array[self.pointer] = ord(sys.stdin.read(1))
    def output(self):
        sys.stdout.write(chr(self.array[self.pointer]))
        
    # actual executors
    def run(self, code, split=False, splitter=" "):
        self.code = code.split(splitter) if split else list(code)
        translated = list(filter(None, [self.dialect.get(c) for c in self.code]))
       
        index, loops = 0, []
        reference = [self.right, self.left, self.plus, self.minus, self.output, self.input]
        
        while not index > len(translated) - 1:
            if self.debugger:
                self.debugger.update(self.array, self.code, index)

            if translated[index] == 7:
                if self.array[self.pointer] == 0:
                    index += translated[index:].index(8) - index
                    continue
                else:
                    loops.append(index)
            
            if translated[index] == 8:
                if not loops:
                    raise SyntaxError()
                
                if self.array[self.pointer] != 0:
                    index = loops[-1] + 1
                    continue
                else:
                    loops.pop()

            function = reference[translated[index] - 1] if translated[index] - 1 < len(reference) else None

            if function:
                function()
                
            index += 1

with open("hello.bf", "r") as f:
    script = f.read()

stuff = Interpreter()
stuff.run(script)