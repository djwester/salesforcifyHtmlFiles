# salesforcifyHtmlFiles
the script takes .html files output by the D2L documentation program Flare and cleans them up so that they can be embedded into existing saleforce pages

# Usage
## Python
If you have python installed you can call 

```
python salesforcifyHtmlFiles.py -f <name of folder containing html files>
```

## No Python (Windows only)
If you do not have python installed you can either download and unzip salesforcifyHtmlFiles.7z. salesforcifyHtmlFiles.exe will be available in build/exe.win-amd64-3.6

alternately you can download and run the salesforcifyHtmlFiles-0.1-amd64.msi windows installer and then use the resulting salesforcifyHtmlFiles.exe 

You can convert the files by calling the following on the command line (from the folder the .exe is located in)

```
salesforcifyHtmlFiles.exe -f <name of folder containing html files>
```
