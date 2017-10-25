# maze-puzzle-test

Exercise:

Write a program that will output a valid route one could follow to collect all specified items within a map. The map is a json description of set of rooms with allowed path and contained object.
exercize starts with an input of:
json reppresentation of map starting room
list of object to collect

```
Room type allowed fields
  id: Integer
  name: String
  north: Integer //referring to a connected room
  south: Integer //referring to a connected room
  west: Integer  //referring to a connected room
  east: Integer  //referring to a connected room
  objects: List  //of Objects
Object type allowed fields
  name: String //Object Name
```

This is an example of a map:
```
{ "rooms": 
	[
		{ "id": 1, "name": "Hallway", "north": 2, "objects": [] },
		{ "id": 2, "name": "Dining Room", "south": 1, "west": 3, "east": 4,"objects": [] },
		{ "id": 3, "name": "Kitchen","east":2, "objects": [ { "name": "Knife" } ]},
		{ "id": 4, "name": "Sun Room","west":2, "objects": [ { "name": "Potted Plant" } ] }
	]
}

```

This is correct result:
```
+----+-------------+----------------+
| Id | Room        | Obj. collected |
+----+-------------+----------------+
| 2  | Dining Room | None           |
| 1  | Hallway     | None           |
| 2  | Dining Room | None           |
| 3  | Kitchen     | KNIFE          |
| 2  | Dining Room | None           |
| 4  | Sun Room    | POTTED PLANT   |
| 2  | Dining Room | None           |
+----+-------------+----------------+
```

Another example is:
```
{
	"rooms":
	[
		{ "id": 1, "name": "Hallway", "north": 2, "east":7, "objects": [] },
		{ "id": 2, "name": "Dining Room", "north": 5, "south": 1, "west": 3, "east": 4, "objects": [] },
		{ "id": 3, "name": "Kitchen","east":2, "objects": [ { "name": "Knife"} ] },
		{ "id": 4, "name": "Sun Room","west":2, "north":6, "south":7,"objects": [] },
		{ "id": 5, "name": "Bedroom","south":2, "east":6, "objects": [{"name": "Pillow" }] },
		{ "id": 6, "name": "Bathroom","west":5, "south":4, "objects": [] },
		{ "id": 7, "name": "Living room","west":1, "north":4, "objects": [{"name": "Potted Plant" }] }
	]
}

```

This is correct result:
```
+----+-------------+----------------+
| Id | Room        | Obj. collected |
+----+-------------+----------------+
| 2  | Dining Room | None           |
| 5  | Bedroom     | None           |
| 2  | Dining Room | None           |
| 1  | Hallway     | None           |
| 2  | Dining Room | None           |
| 3  | Kitchen     | KNIFE          |
| 2  | Dining Room | None           |
| 4  | Sun Room    | None           |
| 6  | Bathroom    | None           |
| 4  | Sun Room    | None           |
| 7  | Living room | POTTED PLANT   |
| 4  | Sun Room    | None           |
| 2  | Dining Room | None           |
| 1  | Hallway     | None           |
| 7  | Living room | POTTED PLANT   |
| 5  | Bedroom     | None           |
| 6  | Bathroom    | None           |
+----+-------------+----------------+
```

To run via docker, please use following:
docker run --rm -v /PATH/FILE.json:/usr/src/maze-puzzle/MY_DATA.json matteuz/maze-puzzle-test /usr/src/maze-puzzle/YOUR_DATA.json START "OBJ 1" "OBJ 2"


Go to https://hub.docker.com/r/matteuz/maze-puzzle-test/ for details about Docker.