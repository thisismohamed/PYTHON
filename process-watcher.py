import psutil
import time

def get_current_processes():
    return {(p.name(), p.pid) for p in psutil.process_iter()}

def main():
    current_processes = get_current_processes()
    print("Current processes:")
    for process, pid in current_processes:
        print(f"{process} (PID: {pid})")       
    while True:
        time.sleep(5)                                  updated_processes = get_current_processes()
        new_processes = updated_processes - current_processes
        if new_processes:
            print("\nNew processes started:")
            for process, pid in new_processes:
                print(f"{process} (PID: {pid})")

        stopped_processes = current_processes - updated_processes
        if stopped_processes:
            print("\nProcesses stopped:")
            for process, pid in stopped_processes:
                print(f"{process} (PID: {pid})")

        current_processes = updated_processes

if __name__ == "__main__":
    main()
