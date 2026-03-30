import tkinter as tk,os,shutil,sys,subprocess as sp
try:import ctypes
except:print("Failed to import 'ctypes'")

def ask(question=''):
    ans="."
    while not ans.strip().lower()in['y','n','yes','no']:ans=input(f'{question} (Y/N): ')
    return ans.strip().lower()in['y','yes']

def is_admin():
    try:return ctypes.windll.shell32.IsUserAnAdmin()
    except:return False

if not is_admin():
    if ask('Compiler is running without admin permissions. Do you want to continiue anyway?')==False:
        try:ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable," ".join(sys.argv),None,1)
        except:print('Unable to switch to admin.')
        sys.exit(0)

dir=os.path.dirname(sys.argv[0]).replace('\\','/')

from tkinter import filedialog
root=tk.Tk()
root.withdraw()

def check_directory_permissions(directory_path='.'):
    result={}
    if os.access(directory_path,os.R_OK):result.update({'r':True})
    else:result.update({'r':False})
    if os.access(directory_path,os.W_OK):result.update({'w':True})
    else:result.update({'w':False})
    if os.access(directory_path,os.X_OK):result.update({'x':True})
    else:result.update({'x':False})
    return result

folder=filedialog.askdirectory()

if len(folder)<1:print('A folder is required.');sys.exit(1)
print(f'"{folder}" chosen')
if check_directory_permissions(folder)['r']==False:print(f'Missing read permission for "{folder}"');sys.exit(1)

if os.path.exists(f'{dir}/pack'):
    if check_directory_permissions(f'{dir}/pack')['w']==False:print("Missing write permission for 'pack'");sys.exit(1)
    print("removing old 'pack' folder")
    shutil.rmtree(f'{dir}/pack')
    print("old 'pack' folder removed")

print(f'copying pack folder from "{folder}"')
shutil.copytree(folder,f'{dir}/pack')
print('pack folder copied')

if os.path.isfile(f'{dir}/packsquash.toml'):
    if check_directory_permissions(f'{dir}/packsquash.toml')['w']==False:print("Missing write permission for 'packsquash.toml'");sys.exit(1)
    print("removing old 'packsquash.toml' file")
    os.remove(f'{dir}/packsquash.toml')
    print("old 'packsquash.toml' file removed")

print("creating temporary 'packsquash.toml'")
open(f'{dir}/packsquash.toml','w').write(f'''pack_directory="{dir}/pack"
zip_compression_iterations=255
recompress_compressed_files=true
output_file_path="{dir}/pack.zip"

["**/*?.txt"]
force_include=true

["assets/**"]
force_include=true

["data/**"]
force_include=true

["META-INF/**"]
force_include=true

["**.json"]
force_include=true
''')
print("temporary 'packsquash.toml' created")

print("running 'packsquash.exe'")
try:
    sp.call(f'"{dir}/packsquash.exe" "{dir}/packsquash.toml"')
    print("'packsquash.exe' complete")
except Exception as e:print(f"unable to run 'packsquash.exe': {e}")

print("removing 'pack' folder")
shutil.rmtree(f'{dir}/pack')
print("'pack' folder removed")

print("removing 'packsquash.toml'")
os.remove(f'{dir}/packsquash.toml')
print("'packsquash.toml' removed")

input('Done...')