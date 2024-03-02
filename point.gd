extends "res://Wave.gd"

var id
var h
var v = 0

func _init(_id):
	id = _id

func _physics_process(delta):
	h = get_point_position(id).y + 200
	
	if v != 0:
		set_point_position(id, Vector2(get_point_position(id).x, (h+v*delta)))
