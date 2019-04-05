# trafficlights

[![Build Status](https://travis-ci.org/hubrigant/trafficlights.svg?branch=master)](https://travis-ci.org/hubrigant/trafficlights)

Playing around with optimizing traffic light timing

The scenario being modeled is a set of four roads (L1, L2, R1, and R2) that all converge on a single exit (E) by way of three convergence intersections (L, R, and C). The two "funnel" roads (L and R) funnel traffic into the exit itself.

```
         L2     R2
          |     |
          |  C  |
    L1----+--+--+---- R1
          L  |  R
             |
             E
```
Each intersection act as both an XOR gate (only one of the two inputs can move/drain at a time) and as a small buffer, holding up to three cars. Cars can flow from input to output if:

a) The intersection gate is open in its direction
b) The output segment is not full
c) The intersection buffer is not full

The four input roads and the exit are considered to have infinite capacity. Funnel road L can hold five cars. Funnel road R can hold 10.

Cars have four possible states: waiting, reacting, moving, and exited. When moving, all cars move at the same speed, but each car has its own latency delay between when it's first possible to move and when it actually moves. The latency is randomly assigned in the range of 1-5. It takes a car 5 ticks to travel 3 car lengths (i.e. the distance across an intersection), although this is likely only relevant at the beginning of the simulation before the funnel roads have filled.
