Found a logic puzzle online. Solved it by pen and paper but felt like it would be an intersting question for me to solve in python as I am learning it recently 🫡.

Question:
There are 3 water jugs, 2 of them have a capacity of 8 Litres, the remaining one has a capacity of 3 Litres. There are also 4 persons each holding a cup of infinite capacity.

Currently, the 2 8-Litre jugs are filled with water. Your goal is to pour water into the cups using the jugs, such that each person would have exactly 4L of water in their cups.
You can pour water from jugs to jugs, or from jugs to cups. However, once the water is poured into a cup, you cannot pour water out of that cup(You can still pour water into the cup though).

Solution:
<details>
  (8L jug, 8L jug, 3L jug, cup1, cup2, cup3, cup4)<br/>
  (5, 8, 3, 0, 0, 0, 0),<br/>
  (5, 8, 0, 3, 0, 0, 0),<br/>
  (2, 8, 3, 3, 0, 0, 0),<br/>
  (0, 8, 3, 3, 2, 0, 0),<br/> 
  (3, 8, 0, 3, 2, 0, 0),<br/>
  (3, 5, 3, 3, 2, 0, 0),<br/> 
  (6, 5, 0, 3, 2, 0, 0),<br/> 
  (6, 2, 3, 3, 2, 0, 0),<br/> 
  (8, 2, 1, 3, 2, 0, 0),<br/> 
  (8, 2, 0, 4, 2, 0, 0),<br/> 
  (5, 2, 3, 4, 2, 0, 0),<br/> 
  (0, 7, 3, 4, 2, 0, 0),<br/> 
  (3, 7, 0, 4, 2, 0, 0),<br/> 
  (3, 4, 3, 4, 2, 0, 0),<br/> 
  (6, 4, 0, 4, 2, 0, 0),<br/> 
  (6, 1, 3, 4, 2, 0, 0),<br/> 
  (6, 0, 3, 4, 2, 1, 0),<br/> 
  (8, 0, 1, 4, 2, 1, 0),<br/> 
  (8, 0, 0, 4, 2, 1, 1),<br/> 
  (5, 0, 3, 4, 2, 1, 1),<br/>
  (5, 0, 0, 4, 2, 4, 1),<br/> 
  (2, 0, 3, 4, 2, 4, 1),<br/> 
  (0, 0, 3, 4, 4, 4, 1),<br/> 
  (0, 0, 0, 4, 4, 4, 4)
</details>

