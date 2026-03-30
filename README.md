# packsquash-automator
Automates a lot of the stuff for packsquash.exe
## Dependencies
* **[packsquash.exe](https://github.com/ComunidadAylas/PackSquash)**  
* **Python 3.9+** (I personally use 3.14)
# How to use
On windows: Disable 'windows smart app control'.  
  
Make sure that you have Python installed.  
Put the `compiler.py` next to the `packsquash.exe`.  
Right-click and open the current folder in the Terminal. (it is also possible to just double-click the `compiler.py` but due to some permission issues it is recommended to run from the terminal)  
Do `python ./compiler.py` to run the compiler.  
  
You will now see a popup about admin permissions, just type "y" or "yes" and press enter.  
A window will pop up asking you to select a folder. Select the folder you wish to pack.  

Now the script will automatically make a copy of the folder and a `packsquash.toml` and then run the `packsquash.exe`.  
It will attempt to delete the folder and file once done but if it fails you can just remove them yourself.  
## Current `packsquash.toml`  
note: `{dir}` is the directory that the `compiler.py` is located in.  
```toml
pack_directory="{dir}/pack"
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
```
