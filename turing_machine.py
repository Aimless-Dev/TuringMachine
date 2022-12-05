class TuringMachine:
    def __init__(self, state = None, #estados de la maquina de turing
                blank = None, #simbolo blanco de el alfabeto dela cinta
                rules = [],   #reglas de transicion
                tape = [],    #cinta
                final = None,  #estado valido y/o final
                pos = 0):#posicion siguiente de la maquina de turing:
        
        self.state = state
        self.blank = blank
        self.rules = rules
        self.tape  = tape
        self.final = final
        self.pos   = pos
        self.start()


    def start(self):
        st = self.state
        if not self.tape: self.tape = [self.blank]
        if self.pos < 0: self.pos += len(self.tape)
        if self.pos >= len(self.tape) or self.pos < 0: raise Error ('Se inicializa mal la posicion')

        self.rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in self.rules)
        """
            Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
            p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
        """

        while True:
            print(st, '\t', end=" ")
            for i, v in enumerate(self.tape):
                if i == self.pos: print("[%s]"%(v,),end=" ")
                else: print(v, end=" ")
            print()

            if st == self.final: break
            if (st, self.tape[self.pos]) not in self.rules: break
            
            (v1, dr, s1) = self.rules[(st, self.tape[self.pos])]
            
            self.tape[self.pos] = v1
            if dr == 'left':
                if self.pos > 0: self.pos -= 1
                else: self.tape.insert(0, self.blank)
            if dr == 'right':
                self.pos += 1
                if self.pos >= len(self.tape): self.tape.append(self.blank)

            st = s1


demo = TuringMachine(
    state   = 'p', #estado inicial de la maquina de turing
    blank   = 'b', #simbolo blanco del alfabeto de la cinta
    tape    = list('1011'), #inserta los elementos en la cinta
    final   = 'q', #estado valido y/o final
    rules   = map( #reglas de transicion
        tuple, [
            "p 1 x right p".split(),
            "p 0 0 right p".split(),
            "p b b right q".split(),
        ]
    )
)