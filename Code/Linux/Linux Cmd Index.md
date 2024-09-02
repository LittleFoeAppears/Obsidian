## **Categories**

##### **[[(L) Help]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Help 
```
##### **[[(L) Navigation]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Navigation 
```
##### **[[(L) File Operation]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/FileOperation 
```
##### **[[(L) System]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/System  
```
##### **[[(L) User]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/User 
```
##### **[[(L) Permission]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Permission  
```
##### **[[(L) Compression]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Compression  
```
##### **[[(L) Remote]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Remote  
```
##### **[[(L) Process Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/ProcessManagement  
```
##### **[[(L) Package Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/PackageManagement 
```
##### **[[(L) Environment Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/EnvironmentManagement  
```
##### **[[(L) Text Editor]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/TextEditor  
```
##### **[[(L) Misc]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #LinuxCmd  and #CmdCategory/Misc 
```

##
---
## **Full List**
```dataview
LIST WITHOUT ID
"**" + file.link + "** : ``" + description + "``" 
FROM #LinuxCmd 
SORT file.name asc
```