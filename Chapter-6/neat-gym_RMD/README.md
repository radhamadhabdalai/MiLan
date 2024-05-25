# Om Sree Sree Ganeshay Namoh
# Om Sree Sree Bankeswaray Namoh
# om Sree Sree Nrusinghay Laxmipataye Namoh

## Self balancing inverted pendulum (cartpole project) 
Reinforcement Learning begins

We will move gradually through theories and program. First just have a look at this fantastic carpole program running through genetic algorithm(NEAT). You will be introduced to OpenGym environment also.
# This work is cloned from simondlevy github
At first install [neat-python](https://github.com/CodeReclaimers/neat-python) 
and [PUREPLES](https://github.com/ukuleleplayer/pureples) from source. 

Then do the following:

Special Notes :- 
1. Python - 3.8
2. pureplas requires gym 0.25.2
3. neat-python (No issue in installation)

4. For 'graphviz' install in conda or in shell command


```
% python3 neat-evolve.py config/cartpole
```
This will run neat-python on the [CartPole-v1](https://gym.openai.com/envs/CartPole-v1/) environment using the
[parallel fitness evaluator](https://neat-python.readthedocs.io/en/latest/module_summaries.html#parallel),
so you can take advantage of all the cores on your computer.

Once evolution finishes, you can try out your evolved network by doing:

```
% python3 neat-test.py models/CartPole-v1<fitness>.dat
```

where ```<fitness>``` is the fitness of your evolved network.
The ```visuals``` folder will contain a PDF showing the corresponding model.


Copyright (c) 2023, 2024 Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in


