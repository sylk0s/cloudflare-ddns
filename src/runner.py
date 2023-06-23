import time

# implements functionality to run a python file in the Runner
class Runnable:
    
    def __init__(self, last_exec, wait_time):
        # the last time this task was executed
        self.last_exec = last_exec
        # the time between executions
        self.wait_time = wait_time

    def should_run(self):
        return self.last_exec + self.wait_time >= time.time()
           

    def try_run(self):
        if self.should_run():
            self.last_exec = time.time()
            self.run()

    def run(self):
        raise NotImplementedError("Classes must extends the runnable and override this method")

# Runs some task
class Runner:

    def __init__(self, config):
        self.config = config
        self.tasks = self.initialize_tasks()

    def initialize_tasks(self):
        pass

    def run_tasks(self, config):
        while True:
            for task in tasks:
                task.try_run()

    def add_task(self, task: Runnable):
        self.tasks.add(task)

    def remove_task(self, task: Runnable):
        self.tasks.remove(task)