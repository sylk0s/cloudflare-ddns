from datetime import datetime, timedelta
import time

# implements functionality to run a python file in the Runner
class Runnable:
    
    def __init__(self, wait_time):
        # the last time this task was executed
        self.last_exec = datetime.now()
        # the time between executions
        self.wait_time = timedelta(minutes=wait_time)

    def should_run(self):
        return self.last_exec + self.wait_time <= datetime.now()
           

    def try_run(self):
        if self.should_run():
            #print("should run task...")
            self.last_exec = datetime.now()
            self.run()
            #print("will run again at ", self.last_exec + self.wait_time)

    def run(self):
        raise NotImplementedError("Classes must extends the runnable and override this method")

# Runs some task
class Runner:

    def __init__(self, tasks):
        self.tasks = tasks

    def __init__(self):
        self.tasks = []

    def run_tasks(self):
        while True:
            #print("running tasks...")
            for task in self.tasks:
                task.try_run()
            time.sleep(1)


    def add_task(self, task: Runnable):
        self.tasks.append(task)

    def remove_task(self, task: Runnable):
        self.tasks.remove(task)