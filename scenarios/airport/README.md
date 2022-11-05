# Loading a luggage to a plane

## Requirements

We have a list of bags that are supposed to be loaded into the plane in containers. 
- The bags are porvided as **a list**
- The bag has only **single attribute - weight**
- Empty bags (weight = 0) and overweight (weight > **40**) can be provided in the list but they should be skipped
- The container can hold multiple bags up to total wieght of **40** kg
- If the next bag in order cannot be fit into container due to crossing **40** kg limit the new container should be provided
- The bags are put into container in the **FIFO** order but unloded in **LIFO** order
- The containers are put into plane in the **FIFO** order but unloded in **LIFO** order

## Problem statement
Write the code* that loads bags into the plane and then unload them.

**Ideally if besides of the main code you provide some unit test as well*

For instance:

Input (the list of bags): **[5, 10, 15, 20, 10, 5]**

Should be split into two containers: [5, 10, 15] *(total wieght 30)* and [20, 10, 5] *(total weight 35)*
During the unload we use LIFO order so first goes the container **[20, 10, 5]** and then container **[5, 10, 15]**, and the once we unload bags from containers as well, finally we should get the output list: **[5, 10, 20, 15, 10, 5]**.
