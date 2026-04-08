import os
import subprocess

def run_python_file(working_directory,file_path,args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path[-3:] == '.py':
        return f'Error: "{file_path}" is not a Python file'
    command = ['python3',target_dir]
    if args != None:
        command.extend(args)
    output = subprocess.run(command,text=True,cwd=abs_working_dir,capture_output=True,timeout=30)
    return_string = f'STDOUT: {output.stdout} STDERR: {output.stderr}'
    if output.returncode != 0:
        return_string += f' Process exited with code {output.returncode}'  
    if output.stdout == "":
        return_string = 'No output produced.'
    return return_string