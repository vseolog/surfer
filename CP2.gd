extends CollisionPolygon2D

var wave = load("res://Wave.gd")
var array = wave.array

func _ready():
	PoolVector2Array().append_array(array)


func _physics_process(delta):
	for i in PoolVector2Array():
		var index = PoolVector2Array().find(i)
		if index != -1:
			PoolVector2Array().insert(index, array[index])
