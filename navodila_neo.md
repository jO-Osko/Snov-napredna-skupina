Naredi si sandbox za neo4j na: https://neo4j.com/sandbox/

Osnovna sintaksa
TODO

Najdi vse filme in njihove igralce:
- Od leta 1991 naprej
- V 70h letih 20 stoletja
- Najdi vse filme in igralce, 
- Najdi vse filme in igralce, ki so bili med igranjem v filmu stari manj kot 30 let
- isto kot zgoraj ampak stari med 40 in 50


```
// To najde....
MATCH (film:Movie)<-[:ACTED_IN]-(oseba)
WITH (film.released - oseba.born) AS starostOsebe, film, oseba
WHERE starostOsebe < 50 AND starostOsebe > 40
RETURN film, oseba
```
```
// To najde....
MATCH (film:Movie)<-[:ACTED_IN|:DIRECTED]-(oseba)
WITH (film.released - oseba.born) AS starostOsebe, film, oseba
WHERE starostOsebe < 50 AND starostOsebe > 40
RETURN film, oseba
```

```
// To najde....
MATCH 
	(film:Movie)<-[:ACTED_IN]-(oseba),
                              (oseba)-[:DIRECTED]->(film2:Movie)
WHERE film <> film2		 
RETURN film, oseba, film2
```

Najdi vse ljudi, ki so režisirali filme v katerih je igral "Tom Hanks

```
MATCH 
	(tom:Person)-[:ACTED_IN]->(:MOVIE)<-[:DIRECTED]-(r:Person)
	WHERE tom.name = "Tom Hanks"
RETURN r
```
Six levels of Kevin Bacon
```
MATCH 
	(kevin:Person)-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(level1)-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(level2)-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(level3)
WHERE kevin.name = "Kevin Bacon"
REturn kevin, level1, level2, level3
```
