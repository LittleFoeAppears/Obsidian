##### Example of Dynamic List

```dataview
LIST
description  
FROM #Example 
SORT file.name asc
```

##### Example sorted by type


```dataview
LIST 
rows.file.link 
FROM #Example 
GROUP BY type
```