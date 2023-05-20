"""
VMO Lab.
Petite-Language Interpreter
"""
from .ixx import *
from .utils import *
from .virtual_machine import VM

import operator


class PTVM(VM):
    """
    Petite Virtual Machine
    """
    INT_TYPE = int

    def __init__(self):
        """
            Operator precedence.
            0. '(', ')', '[', ']'
            1. '*', '/'
            2. '+', '-'
            3. '==', '!=', '<', '>', '<=', '>='
        """
        super().__init__()
        op0 = {'(': None, ')': None,
               '[': lambda x, n: operator.getitem(x, int(n)), ']': None}
        op1 = {'*': operator.mul, '/': operator.truediv}
        op2 = {'+': operator.add, '-': operator.sub}
        op3 = {'==': operator.eq, '!=': operator.ne,
               '<': operator.lt, '>': operator.gt,
               '<=': operator.le, '>=': operator.ge}
        self.operators = [op0, op1, op2, op3]  # Operator table.

    def scan_labels(self):
        # TODO
        pass

    # TODO
