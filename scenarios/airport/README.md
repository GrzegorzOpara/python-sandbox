# Loading luggage to a plane

## Requirements

We have a list of bags that are supposed to be loaded into the plane in containers. 
- The bags are provided as **a list**
- The bag has only **single attribute - weight**
- Empty bags (weight = 0) and overweight (weight > **40**) can be provided in the list, but they should be skipped
- The container can hold multiple bags up to a total weight of **40** kg
- If the next bag in order cannot fit into the container due to crossing **40** kg limit, the new container should be provided
- The bags are put into container in the **FIFO** order but unloaded in **LIFO** order
- The containers are put into a plane in the **FIFO** order but unloaded in **LIFO** order

## Problem statement
Write the code* that loads bags into the plane and then unloads them.

**Ideally, if besides the main code, you provide some unit tests as well*

For instance:

Input (the list of bags): **[5, 10, 15, 20, 10, 5]**

Should be split into two containers: [5, 10, 15] *(total weight 30)* and [20, 10, 5] *(total weight 35)*
During the unload, we use LIFO order, so first goes the container **[20, 10, 5]** and then container **[5, 10, 15]**, and then once we unload bags from containers as well, finally we should get the output list: **[5, 10, 20, 15, 10, 5]**.
