import subprocess

path = r"C:\Users\DARGON2\Desktop\proje resim python"
tasks = ["raspery_veri.py"]
task_processes = [
    subprocess.Popen(r'python %s\%s' % (path, task), shell=True)
    for task
    in tasks
]
for task in task_processes:
    task.wait()