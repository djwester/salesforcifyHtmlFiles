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

alternately you can download and run the .msi windows installer and then use the resulting salesforcifyHtmlFiles.exe 

You can convert the files by calling the following on the command line

```
"C:\Program Files\salesforcifyHtmlFiles\salesforcifyHtmlFiles.exe" -f <name of folder containing html files>
```
assuming of course, that you have it installed in C:\Program Files

### Re-installing
If you have already run the installer and there is a new update you would like to get you can uninstall the current version of salesforcifyHtmlFiles, by going to add/remove programs in the control panel and calling Right Click>Uninstall on the salesforcifyHtmlFiles program.

Once you have uninstalled it, you can just run the installer again to get the latest version

# Making Changes
If you want to make changes you can edit the python file. There are no tests, so you will just have to manually run the file to test out your changes.

Once you have made the changes you can rebuil the .msi.

To do this, first update the version number in the setup.py file and then build by calling

```
python setup.py bdist_msi
```