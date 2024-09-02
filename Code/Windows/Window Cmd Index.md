## **Categories**

##### **[[(w) Help]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Help 
```
##### **[[(w) Navigation]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Navigation 
```
##### **[[(w) File Operation]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/FileOperation 
```
##### **[[(w) System]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/System  
```
##### **[[(w) User]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/User 
```
##### **[[(w) Permission]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Permission  
```
##### **[[(w) Compression]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Compression  
```
##### **[[(w) Remote]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Remote  
```
##### **[[(w) Process Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/ProcessManagement  
```
##### **[[(w) Package Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/PackageManagement 
```
##### **[[(w) Environment Management]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/EnvironmentManagement  
```
##### **[[(w) Text Editor]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/TextEditor  
```
##### **[[(w) Misc]]**
```dataview
LIST WITHOUT ID
"**" + file.link + "**" + " :  ``" + description + "``"
FROM #WindowsCmd   and #CmdCategory/Misc 
```

##
---
## **Full List**
```dataview
LIST WITHOUT ID
"**" + file.link + "** : ``" + description + "``" 
FROM #WindowsCmd  
SORT file.name asc
```