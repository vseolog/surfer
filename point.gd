extends Line2D

var id
var h
var v = 0

func _init(_id):
	id = _id
	h = get_point_position(id).y

func _process(delta):
	h = get_point_position(id).y
	if v != 0:
		set_point_position(id, Vector2(get_point_position(id).x, (h+v)))
