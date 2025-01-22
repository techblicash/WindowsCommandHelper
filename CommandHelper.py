import subprocess
import tkinter as tk
from tkinter import messagebox

def execute_powershell_get_process():
    try:
        command = "powershell Get-Process"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_powershell_get_service():
    try:
        command = "powershell Get-Service"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_powershell_check_updates():
    try:
        command = "powershell Get-WindowsUpdateLog"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_powershell_list_files():
    path = parameter_entry.get()
    if not path.strip():
        path = "C:\\"  # Default to root directory

    command = f"powershell Get-ChildItem -Path {path}"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_ping():
    target = parameter_entry.get()
    packet_size = packet_size_entry.get()
    count = count_entry.get()
    continuous = continuous_var.get()

    if not target.strip():
        messagebox.showwarning("Warning", "Please enter a target to ping.")
        return

    command = f"ping {target}"
    if packet_size.strip():
        try:
            packet_size = int(packet_size)
            if packet_size < 1 or packet_size > 65500:
                messagebox.showerror("Error", "Packet size must be between 1 and 65500 bytes.")
                return
            command += f" -l {packet_size}"
        except ValueError:
            messagebox.showerror("Error", "Invalid packet size. Please enter a numeric value.")
            return
    if count.strip():
        command += f" -n {count}"
    if continuous:
        command += f" -t"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_traceroute():
    target = parameter_entry.get()
    max_hops = max_hops_entry.get()
    timeout = timeout_entry.get()

    if not target.strip():
        messagebox.showwarning("Warning", "Please enter a target for traceroute.")
        return

    command = f"tracert {target}" if subprocess.os.name == "nt" else f"traceroute {target}"
    if max_hops.strip():
        command += f" -h {max_hops}"
    if timeout.strip():
        command += f" -w {timeout}"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_ipconfig():
    try:
        command = "ipconfig" if subprocess.os.name == "nt" else "ifconfig"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_netstat():
    show_all = show_all_var.get()
    command = "netstat -a" if subprocess.os.name == "nt" else "ss -a"
    if show_all:
        command += " -n"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_tasklist():
    filter_process = filter_entry.get()
    command = "tasklist" if subprocess.os.name == "nt" else "top -b -n 1"
    if filter_process.strip():
        if subprocess.os.name == "nt":
            command += f" | findstr {filter_process}"
        else:
            command += f" | grep {filter_process}"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_dns_lookup():
    target = parameter_entry.get()
    if not target.strip():
        messagebox.showwarning("Warning", "Please enter a domain for DNS lookup.")
        return

    command = f"nslookup {target}"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_disk_usage():
    command = "wmic logicaldisk get size,freespace,caption" if subprocess.os.name == "nt" else "df -h"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_date_time():
    command_date = "date /T" if subprocess.os.name == "nt" else "date"
    command_time = "time /T" if subprocess.os.name == "nt" else "date +'%T'"

    try:
        result_date = subprocess.run(command_date, shell=True, capture_output=True, text=True, encoding="utf-8")
        result_time = subprocess.run(command_time, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result_date.stdout:
            output_text.insert(tk.END, f"Date Output:\n{result_date.stdout.strip()}\n")
        if result_time.stdout:
            output_text.insert(tk.END, f"Time Output:\n{result_time.stdout.strip()}\n")
        if result_date.stderr or result_time.stderr:
            output_text.insert(tk.END, f"Error:\n{result_date.stderr}{result_time.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_install_package():
    package_name = parameter_entry.get()
    if not package_name.strip():
        messagebox.showwarning("Warning", "Please enter the name of the Python package to install.")
        return

    command = f"pip install {package_name}"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

def execute_custom_command():
    command = parameter_entry.get()
    if not command.strip():
        messagebox.showwarning("Warning", "Please enter a command to execute.")
        return
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8")
        output_text.delete(1.0, tk.END)
        if result.stdout:
            output_text.insert(tk.END, f"Output:\n{result.stdout}\n")
        if result.stderr:
            output_text.insert(tk.END, f"Error:\n{result.stderr}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred:\n{e}\n")

# Create the main GUI window
root = tk.Tk()
root.title("Command Helper")

# Add instructions
instruction_label = tk.Label(root, text="请选择操作并输入必要的参数：")
instruction_label.pack(pady=5)

# Dropdown menu for actions
def on_action_change(event):
    selected_action = action_var.get()
    if selected_action == "测试连接":
        parameter_label.config(text="请输入目标地址（例如 www.example.com）:")
        advanced_ping_frame.pack(pady=5)
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "路由追踪":
        parameter_label.config(text="请输入目标地址（例如 www.example.com）:")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack(pady=5)
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "查看IP配置":
        parameter_label.config(text="此操作无需输入参数。")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "端口扫描":
        parameter_label.config(text="此操作无需输入参数。")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack(pady=5)
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "系统资源监控":
        parameter_label.config(text="此操作无需输入参数。")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack(pady=5)
    elif selected_action == "DNS解析测试":
        parameter_label.config(text="请输入目标域名（例如 www.example.com）:")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "磁盘使用情况":
        parameter_label.config(text="此操作无需输入参数。")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "系统时间与日期":
        parameter_label.config(text="此操作无需输入参数。")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "安装Python包":
        parameter_label.config(text="请输入要安装的Python包名称：")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()
    elif selected_action == "自定义指令":
        parameter_label.config(text="请输入自定义指令：")
        advanced_ping_frame.pack_forget()
        advanced_traceroute_frame.pack_forget()
        advanced_netstat_frame.pack_forget()
        advanced_tasklist_frame.pack_forget()

action_var = tk.StringVar(value="请选择")
actions = ["请选择", "测试连接", "路由追踪", "查看IP配置", "端口扫描", "系统资源监控", "DNS解析测试", "磁盘使用情况", "系统时间与日期", "安装Python包", "自定义指令","查看进程", "查看服务", "检查更新日志", "列出文件"]
action_menu = tk.OptionMenu(root, action_var, *actions, command=on_action_change)
action_menu.pack(pady=5)

# Parameter input
parameter_label = tk.Label(root, text="请输入目标地址（例如 www.example.com）:")
parameter_label.pack(pady=5)
parameter_entry = tk.Entry(root, width=50)
parameter_entry.pack(pady=5)

# Advanced options for ping
advanced_ping_frame = tk.Frame(root)
packet_size_label = tk.Label(advanced_ping_frame, text="数据包大小（字节，1-65500）：")
packet_size_label.grid(row=0, column=0, padx=5, pady=5)
packet_size_entry = tk.Entry(advanced_ping_frame, width=10)
packet_size_entry.grid(row=0, column=1, padx=5, pady=5)

count_label = tk.Label(advanced_ping_frame, text="发送数据包数量：")
count_label.grid(row=1, column=0, padx=5, pady=5)
count_entry = tk.Entry(advanced_ping_frame, width=10)
count_entry.grid(row=1, column=1, padx=5, pady=5)

continuous_var = tk.BooleanVar()
continuous_check = tk.Checkbutton(advanced_ping_frame, text="持续发送数据包", variable=continuous_var)
continuous_check.grid(row=2, column=0, columnspan=2, pady=5)

# Advanced options for traceroute
advanced_traceroute_frame = tk.Frame(root)
max_hops_label = tk.Label(advanced_traceroute_frame, text="最大跳数：")
max_hops_label.grid(row=0, column=0, padx=5, pady=5)
max_hops_entry = tk.Entry(advanced_traceroute_frame, width=10)
max_hops_entry.grid(row=0, column=1, padx=5, pady=5)

timeout_label = tk.Label(advanced_traceroute_frame, text="超时时间（秒）：")
timeout_label.grid(row=1, column=0, padx=5, pady=5)
timeout_entry = tk.Entry(advanced_traceroute_frame, width=10)
timeout_entry.grid(row=1, column=1, padx=5, pady=5)

# Advanced options for netstat
advanced_netstat_frame = tk.Frame(root)
show_all_var = tk.BooleanVar()
show_all_check = tk.Checkbutton(advanced_netstat_frame, text="显示所有连接", variable=show_all_var)
show_all_check.grid(row=0, column=0, columnspan=2, pady=5)

# Advanced options for tasklist
advanced_tasklist_frame = tk.Frame(root)
filter_label = tk.Label(advanced_tasklist_frame, text="过滤进程名或PID：")
filter_label.grid(row=0, column=0, padx=5, pady=5)
filter_entry = tk.Entry(advanced_tasklist_frame, width=20)
filter_entry.grid(row=0, column=1, padx=5, pady=5)

# Run button
def run_action():
    selected_action = action_var.get()
    if selected_action == "请选择":
        messagebox.showwarning("Warning", "请选择要执行的指令！")
    elif selected_action == "测试连接":
        execute_ping()
    elif selected_action == "路由追踪":
        execute_traceroute()
    elif selected_action == "查看IP配置":
        execute_ipconfig()
    elif selected_action == "端口扫描":
        execute_netstat()
    elif selected_action == "系统资源监控":
        execute_tasklist()
    elif selected_action == "DNS解析测试":
        execute_dns_lookup()
    elif selected_action == "磁盘使用情况":
        execute_disk_usage()
    elif selected_action == "系统时间与日期":
        execute_date_time()
    elif selected_action == "安装Python包":
        execute_install_package()
    elif selected_action == "查看进程":
        execute_powershell_get_process()
    elif selected_action == "查看服务":
        execute_powershell_get_service()
    elif selected_action == "检查更新日志":
        execute_powershell_check_updates()
    elif selected_action == "列出文件":
        execute_powershell_list_files()
    elif selected_action == "自定义指令":
        execute_custom_command()

# Clear button
def clear_output():
    output_text.delete(1.0, tk.END)

run_button = tk.Button(root, text="运行", command=run_action)
run_button.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="清空输出", command=clear_output)
clear_button.pack(pady=5)

# Output text box
output_text = tk.Text(root, height=20, width=60)
output_text.pack(pady=5)

# Add a scrollbar to the text box
scrollbar = tk.Scrollbar(root, command=output_text.yview)
output_text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the GUI event loop
root.mainloop()
