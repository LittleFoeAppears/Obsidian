#### Sorted list exposing the Description 
```dataview
LIST
" _" + Description + "_"
FROM #Fruit
SORT file.name asc
```

---

#### Sorted list exposing Name and Quantity
```dataview
LIST WITHOUT ID
file.name +"  : **" + Quantity + "**"
FROM #Fruit
SORT Quantity asc
```

---

#### Sorted list also grouped by Familly
```dataview
LIST
rows.file.link
FROM #Fruit
GROUP BY Familly
SORT Quantity asc
```

---

#### Sorted Table exposing Familly and Quantity
```dataview
TABLE 
Familly, Quantity
FROM #Fruit 
SORT Quantity desc
```