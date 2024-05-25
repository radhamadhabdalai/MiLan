######################################################################################
'''Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in'''
###################################################################################
import gym
from neat_gym import read_file, eval_net

# Load genome and configuration from pickled file
net, env_name, record_dir, seed, nodisplay, csvfilename = \
        read_file(allow_record=True, allow_seed=True)

# Run the network on the environment
eval_net(net,
         gym.make(env_name),
         render=(not nodisplay),
         record_dir=record_dir,
         seed=seed,
         csvfilename=csvfilename,
         report=True)
