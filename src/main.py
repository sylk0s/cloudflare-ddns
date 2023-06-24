from clf_io import DynDNSJob
from runner import Runner
from config import ClfJobConfig
from dotenv import load_dotenv
import os

# does some stuff
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