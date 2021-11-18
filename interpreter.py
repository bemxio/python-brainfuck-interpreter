import debugger
import sys

class Interpreter:
    def __init__(self, code, debug=None, size=30000):
        self.array = [0 for _ in range(size)]
        self.pointer = 0
        self.size = size

        self.code = list(code)
        self.debug = debug() if debug else None
    
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
    def run(self):
        reference = {
            ">": self.right,
            "<": self.left,
            "+": self.plus,
            "-": self.minus,
            ",": self.input,
            ".": self.output
        }
        
        i, j = 0, []
        
        while not i > len(self.code) - 1:
            if self.debug:
                self.debug.update(self.array, self.code, i)

            if self.code[i] == "[":
                if self.array[self.pointer] == 0:
                    i += (self.code[i:].index("]") - i)
                    continue
                else:
                    j.append(i)
            
            if self.code[i] == "]":
                if not j:
                    raise SyntaxError()
                
                if self.array[self.pointer] != 0:
                    i = j[-1] + 1
                    continue
                else:
                    j.pop()
            
            function = reference.get(self.code[i]) 
            if function:
                function()
                
            i += 1

with open("hello.bf", "r") as f:
    script = f.read()

stuff = Interpreter(script, debug=debugger.ArrayVisualization)
stuff.run()