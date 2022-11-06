# Beach party
You decided to have a party with your friends on the nearest beach. It's pretty narrow, and there is only a single row of spots between the road and the sea. Some of them are free, the others occupied. You need to ensure there are enough free spots next to each other to fit all your friends together.

## Problem statement
Write the code* gets as input the array of beach spots; the array elements are either *'T' - Taken*, *'F' - Free*.

As a second input, you provide the number of guests coming to the party you want to have, all with a seat next to each other. 

The code should **True** if it's feasible to fit everyone on the beach or **False** if it's not. 

**Ideally if besides the main code, you provide some unit tests as well*

For instance:

Input:
- (['T', 'F', 'F', 'T', 'F', 'F', 'F','T', 'F'], 5) should return False since there are no five consecutive free slots on the beach
- (['T', 'F', 'F', 'T', 'F', 'F', 'F','T', 'F'], 3) should return True since there are three consecutive free slots on the beach