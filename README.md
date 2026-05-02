# packsquash-automator
> Automates a lot of the stuff for packsquash.exe

> [!CAUTION]
> I only made this tool for personal use, I'm probably not going to expand on this or help you if it doesn't work.
## Dependencies
* ~~**[packsquash.exe](https://github.com/ComunidadAylas/PackSquash)**~~ Packsquash is included in script  
* **Python 3.9+** (I personally use 3.14)
# How to use

> [!IMPORTANT]
> Make sure that you have Python installed.

> [!TIP]
> On windows:  
> &ensp;&ensp;Disable 'windows smart app control'.

Right-click and open the folder with the script in the Terminal.  
Do `python ./compiler.py` to run the compiler.  
>[!NOTE]
> It is also possible to just double-click the `compiler.py` but due to some permission issues it is recommended to run from the terminal
  
You will now see a popup about admin permissions, just type "y" or "yes" and press enter.  
A window will pop up asking you to select a folder. Select the folder you wish to pack.  

> It will attempt to delete the `packsquash_spec` folder once done but if it fails you can just remove them yourself.  

> [!NOTE]
> `{dir}` is the directory that the `compiler.py` is located in.  
## Tested Enviorments
* Windows 11, Python 3.14
