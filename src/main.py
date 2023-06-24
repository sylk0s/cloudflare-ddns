from clf_io import DynDNSJob
from runner import Runner
from config import ClfJobConfig

# does some stuff
def main():
    runner = Runner()

    # creates a task
    config = ClfJobConfig("NOPE", "sylkos.xyz", 1, "A", "sylkos.xyz")
    task = DynDNSJob(config)
    runner.add_task(task)

    # runs the runner
    runner.run_tasks()

if __name__ == "__main__":
    main()