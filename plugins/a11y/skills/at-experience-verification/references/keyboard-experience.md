# Keyboard journey evidence

Complete the user's task without a pointer. Record starting focus, every action,
visible focus, meaningful traversal, activation, modal exit and restoration.
Composite widgets may use a single Tab stop and internal arrows
([APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)).

Wrong: every option is forced into the page Tab order.
Right: implement the chosen widget pattern and test forward/reverse movement.
Wrong: focus returns to a removed delete trigger.
Right: choose a surviving logical workflow destination and verify the next action
([APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).
