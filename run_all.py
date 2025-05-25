import subprocess

def run_script(script_name):
    try:
        print(f"Starting {script_name}...")
        process = subprocess.Popen(['python', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stdout:
            print(f"Output of {script_name}:\n{stdout}")
        if stderr:
            print(f"Errors from {script_name}:\n{stderr}")

        print(f"{script_name} finished with exit code {process.returncode}\n")
    except Exception as e:
        print(f"Failed to run {script_name}. Error: {e}")

if __name__ == "__main__":
    scripts = ['app1.py', 'app2.py', 'app3.py', 'app4.py', 'app5.py']
    for script in scripts:
        run_script(script)

