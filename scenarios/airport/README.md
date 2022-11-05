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
Write the code that loads bags into the plane and then unload them.

For instance:

Input: [5, 10, 15, 10, 10, 5]

Should be split into two containers: [5, 10, 15] and [10, 10, 5]
During the unload we use LIFO order so first goes [10, 10, 5] and then [5, 10, 15], and the once we unload bags from containers as well, finally we should get: [15, 10, 5, 5, 10, 10]
