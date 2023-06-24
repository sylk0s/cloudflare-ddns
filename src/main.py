from clf_io import DynDNSJob
from runner import Runner
from config import ClfJobConfig
from dotenv import load_dotenv
import os

# the idea is that eventually we would be able to serialize json or some other filetype into the config, 
# and you would be able to specify multiple jobs for the runner to run, but I decided to leave that for
# the future because my main focus for this application was to package it in a docker container to run on
# my server so my DNS stops breaking... and I couldn't come up with a clean way to pass JSON into a docker
# container. I think in the future I could just make a more complex setup for it, but for now I'm just 
# gonna leave it.

# runs the program
def main():
    load_dotenv()
    runner = Runner()

    # creates a task
    config = ClfJobConfig()
    task = DynDNSJob(config)
    runner.add_task(task)

    # runs the runner
    runner.run_tasks()

if __name__ == "__main__":
    main()