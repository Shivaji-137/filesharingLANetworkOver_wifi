# server_run.py is wriiten by Shivaji Chaulagain for accessing, downloading the files of your pc from another pc or mobile phones  and uploading the files to the pc via wifi (no pendrive, additional secondary storage device needed), connected in same network (in same wifi/router)

## This is the code for reading and downloading files from one pc(not mobile) to another pc or mobile, all devices  must be connected to the same network(same wifi).

### To run:
    ---> You can make only laptop a server(not mobile). Open the laptop. Go to the folder/directory you want to give access of sharing, downloading the files to another devices. Then open the terminal in that folder.
    ---> pip install flask (if not installed. You must have python installed in os)
    ---> if you have no server_run.py file in the folder, copy that file in the folder or specify the full path in python path_of_file
    ---> In your terminal, Type ( it works in both windows and linux):
             python server_run.py               [or if not file in the folder: python /path/to/server_run.py (in linux) or python \path\to\server_run.py (in windows)]
         - if it does not work, type:
             python3 server_run.py    (server_run.py must be in the same folder as your terminal is)
              
                  
             
    ----> Click enter and you will see like this (this output is on my pc): 
             * Running on all addresses (0.0.0.0)
             * Running on http://127.0.0.1:8000
             * Running on http://192.168.1.95:8000    (192.168.1.95 is my laptop address. your ip address could be different)
                                
    ----> Copy or type that url of last output http://192.168.1.95:8000  in another pc or your mobile phone(all phone:android, iphone. Here, your mobile phone, another pc or that pc as a server must be connected to the same wifi). don't use https in the url cz it is not supported here.
    
    ----> Access the files, dowload the files  from the server laptop into your mobile phones or another laptop. You can also upload the files from mobile phones or other devices.
    ----> currently, supported upload files are:
             ALLOWED_EXTENSIONS = {
                    'zip', 'tar', 'gz', 'rar', '7z',                # Compressed files
                    'mp3', 'wav', 'aac', 'flac', 'ogg',             # Audio files
                    'mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',       # Video files
                    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff',     # Image files
                    'pdf'                                           # PDF files
                }
   -----> You can edit the server_run.py and add the desired extensions or filetype name in ALLOWED_EXTENSIONS variable in server_run.py
        
    
