#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --gpus=1
#SBATCH --cpus-per-task=18
#SBATCH --partition=gpu
#SBATCH --time=04:00:00

# Make sure the jupyter command is available, either by loading the appropriate modules, sourcing your own virtual environment, etc.
module load 2022
module load IPython/8.5.0-GCCcore-11.3.0
module load CUDA/11.7.0
 
# Choose random port and print instructions to connect
PORT=`shuf -i 5000-5999 -n 1`
LOGIN_HOST=int4-pub.snellius.surf.nl
BATCH_HOST=$(hostname)
 
echo "To connect to the notebook type the following command from your local terminal:"
echo "ssh -J ${USER}@${LOGIN_HOST} ${USER}@${BATCH_HOST} -L ${PORT}:localhost:${PORT}"
echo
echo "After connection is established in your local browser go to the address:"
echo "http://localhost:${PORT}"

jupyter notebook --no-browser --port $PORT

