extends Line2D

var number_of_points = 500
var screen_leight = 1000
var screen_widght = 600
var y_position = 200.0
var k = 0.1
var array = []


func _ready():
	var point = load('res://point.gd')
	for i in range(1, number_of_points+1):
		var x_position = i*(screen_leight/number_of_points)
		add_point(Vector2(x_position, y_position), i)
		var a = point.new(i)
		array.append(a)


func _physics_process(delta):
	for j in array:
		if j.id != 0 and j.id < len(array)-1:
			j.h = get_point_position(j.id).y
			var p = array[j.id-1]
			var n = array[j.id+1]
			j.v = ((p.h - j.h) + (n.h - j.h)) * delta*50
		if j.v != 0:
			set_point_position(j.id, Vector2(get_point_position(j.id).x, (j.h + (j.v * delta))))


func _input(event):
	if event is InputEventMouseButton and event.is_pressed() and event.button_index == 1:
		var event_x_position = float(event.get_position().x)
		var event_y_position = float(event.get_position().y)
		print('wave created')
		print(event_x_position)
		var event_point_index = int((event_x_position)/((screen_leight)/(number_of_points)))
		print('Index of point: '+ str(event_point_index))
		set_point_position(event_point_index, Vector2(event_x_position, event_y_position-200))
