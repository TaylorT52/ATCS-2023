"""
This module implements a Finite State Machine (FSM).

You define an FSM by building a dictionary of transitions. For a given input symbol,
the process() method uses the dictionary to decide what action to call and what
the next state will be. The FSM has a dictionary of transitions that associate the tuples:

        (input_symbol, current_state) --> (action, next_state)

Where "action" is a function you define. The symbols and states can be any
objects. You use the add_transition() method to add to the transition table.

@author: Ms. Namasivayam
@version: 2022
"""


class FSM:

        
