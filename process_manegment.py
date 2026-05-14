import subprocess
import os
import time

class process:
    def __init__(self, command):
        self.command = command
        self.syntax_error = False
        self.command_found = True


        self.command = command.strip()
        self.command = command.split()

        if (self.command[0] == "run"):
            if (len(self.command) == 2):
                self.run(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "manage_processes"):
            if (len(self.command) == 1):
                self.manage_processes()
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "processes_schedualing"):
            if (len(self.command) == 2):
                self.processes_schedualing(self.command[1])
                return
            else:
                self.syntax_error = True

        elif (self.command[0] == "zombie_process"):
            if (len(self.command) == 1):
                self.zombie_process()
                return
            else:
                self.syntax_error = True

        else:
            self.command_found = False

    def run(self, program):
            try:
                # Popen starts the process in the background
                # We don't use .run() because .run() waits for the program to close
                process = subprocess.Popen(program, shell=True)
                
                # Get the real Process ID assigned by the system
                real_pid = process.pid
                
                print(f"Starting {program}...")
                print(f"Process created with ID: {real_pid}")
                
            except Exception as e:
                 print(f"An error occurred: {e}")


    def manage_processes(self):
        # 1. Use the system's native command to list processes
        cmd = "ps -e"
        
        print("\n--- Process Monitor ---")
        os.system(cmd) 
        
        # 2. Ask for the ID to kill
        target = input("\nEnter PID to kill (or 'c' to cancel): ")
        
        if target == 'c':
            return

        try:
            os.system(f"kill -9 {target}")
            print(f"process {target} has terminated.")
            
        except Exception as e:
                 print(f"An error occurred: {e}")


    def processes_schedualing(sef, mode):
        # We will run two simple pings as our "processes"
        param = "-c"
        cmd1 = ["ping", "127.0.0.1", param, "3"]
        cmd2 = ["ping", "google.com", param, "3"]

        start_time = time.time()

        if mode == "1":
            print("\n--- Running SEQUENTIAL (Wait for each) ---")
            # .run() waits for the process to complete
            report1 = subprocess.run(cmd1, capture_output=True, text=True)
            print("Process 1 Finished.")
            
            report2 = subprocess.run(cmd2, capture_output=True, text=True)
            print("Process 2 Finished.")

        elif mode == "2":
            print("\n--- Running CONCURRENT (Run together) ---")
            # .Popen() starts the process and keeps going
            p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
            p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE)
            
            print("Both processes started simultaneously...")
            
            # We 'wait' at the end just to calculate total time
            p1.wait()
            p2.wait()
            print("Both processes finished.")

        end_time = time.time()
        print(f"\nTOTAL TIME TAKEN: {round(end_time - start_time, 2)} seconds")
        print("-" * 40)


    def zombie_process(self):
        print("\n--- Zombie Process Creator ---")
        
        pid = os.fork()

        if pid > 0:
            # This is the PARENT process
            print(f"[PARENT] Created child with PID: {pid}")
            print(f"[PARENT] we dont call wait() so Child is now a Zombie.")
            print(f"[PARENT] Checking process table for processes...")
            
            # Give the child a second to exit first
            time.sleep(2)
            
            # Show the zombie in the process list
            # We look for "Z" status or "defunct"
            try:
                result = subprocess.check_output(["ps", "-o", "pid,ppid,stat,comm", "-p", str(pid)]).decode()
                print("\nPROCESS TABLE REPORT:")
                print(result)
            except Exception as e:
                print(f"Could not retrieve process info: {e}")

            print("\n[PARENT] Now we will wait for the child to clean it up...")
            os.waitpid(pid, 0)
            print("[PARENT] Child collected. Zombie gone.")
            
        else:
            # This is the CHILD process
            print(f"[CHILD] we are running (PID: {os.getpid()}) and exiting immediately.")
            os._exit(0) # Exit without cleaning up resources