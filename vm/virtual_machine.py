"""
VMO Lab.
Virtual Machine
"""
from .utils import in2post

import pprint
import copy


class VM:
    """
    Virtual Machine
    """
    INT_TYPE = int

    def __init__(self):
        self.pc = 0
        self.mem = {}
        self.code = []
        self.code_lines = 0
        self.operators = []

    def __repr__(self):
        formatted_mem = pprint.pformat(self.mem, indent=2)
        return f'PC: {self.pc}, MEM: {formatted_mem}'

    def load(self, source_file):
        """
        Load code into the machine.
        Strip the whitespaces before saving them.
        """
        with open(source_file, 'r') as f:
            self.code = [line.strip() for line in f]
            self.code_lines = len(self.code)

    def reset(self):
        """
        Reset the machine's state and return current state.
        """
        old_mem = copy.deepcopy(self.mem)
        self.pc = 0
        self.mem = {}
        self.code = []
        self.code_lines = 0
        return old_mem

    def evaluate(self, expr):
        """
        Evaluate the expression's value.
        """
        raise NotImplementedError('`evaluate` is not implemented yet')

    def execute(self, pc, cmdline):
        """
        Execute a single command line and return next PC.
        """
        raise NotImplementedError('`execute` is not implemented yet')

    def calc(self, posfix_expr):
        """
        Calculate the given formula.
        """
        stack = []
        all_ops = {op: act
                   for opgrp in self.operators
                   for op, act in opgrp.items()}

        for t in posfix_expr:
            if t not in all_ops:
                stack.append(self.evaluate(t))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = all_ops[t](operand1, operand2)
                stack.append(self.INT_TYPE(result))

        if len(stack) != 1:
            raise Exception("Illegal Expression")

        return stack[0]

    def compute(self, expr):
        """
        Compute the expression, E @ E
        """
        expr = expr.replace('(', ' ( ').replace(')', ' ) ')
        expr = expr.replace('[', ' [ ').replace(']', ' ] ')
        postfix_expr = in2post(self.operators, expr.split())
        return self.calc(postfix_expr)

    def run(self, breakpoints=set()):
        """
        1. Scan the labels in the program.
        2. Execute line by line until the end of the program.
        *. If current PC is in 'breakpoints' -> Save current PTVM state in the list

        Return the states list.
        """
        raise NotImplementedError('`run` is not implemented')
