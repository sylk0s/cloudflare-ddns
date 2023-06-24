from datetime import datetime, timedelta
import time

class Runnable:
    """
    Some runnable job by the Runner class
    - should never be instantialized, just extended
    - handles generic running logic, but not the implementation of run
    """
    
    def __init__(self, wait_time):
        """Sets up the runnable object"""

        # the last time this task was executed
        self.last_exec = datetime.now()
        # the time between executions
        self.wait_time = timedelta(minutes=wait_time)

# 
    def should_run(self):
        """Determines if a runnable object should be run at this point in time"""

        return self.last_exec + self.wait_time <= datetime.now()
           

    def try_run(self):
        """runs this runnable object should be run, otherwise does nothing"""

        if self.should_run():
            self.last_exec = datetime.now()
            self.run()
            #print("will run again at ", self.last_exec + self.wait_time)

    def run(self):
        """Runs this job"""

        raise NotImplementedError("Classes must extends the runnable and override this method")

# Runs some task
class Runner:
    """
    Object which handles running runnable objects
    """

    def __init__(self, tasks):
        """initializes the tasks of this object"""

        self.tasks = tasks

    def __init__(self):
        """default for if there are no initial tasks"""

        self.tasks = []

    def run_tasks(self):
        """loop to try to run tasks every second"""

        while True:
            for task in self.tasks:
                task.try_run()
            time.sleep(1)


    def add_task(self, task: Runnable):
        """Adds a task to the queue of tasks for this object"""

        self.tasks.append(task)

    def remove_task(self, task: Runnable):
        """Removes a task from the queue of tasks for this object"""
        
        self.tasks.remove(task)