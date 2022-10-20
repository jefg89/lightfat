
import subprocess
import sys


def start_tracing (app_name): 
    # target_pid = subprocess.run(["pidof", app_name], stdout=subprocess.PIPE, text=True).stdout
    # print (target_pid[:-1])
    # output = subprocess.run(["sudo","perf", "stat", "-I 10" , "-e cycles,instructions,cache-references", "-p", target_pid[:-1], "-a" , "-o", "tmp.log", "sleep", "1"], stdout=subprocess.PIPE, text=True)   
    # ####### Now let's create some sub-files
    
    subprocess.run(["cat", "tmp.log", "|", "grep", "cache", ">", "cache.out"])
    subprocess.run(["cat", "tmp.log", "|", "grep", "insn", ">" , "ipc.out"])




if __name__ == '__main__':
    app_name = sys.argv[1]
    start_tracing(app_name)