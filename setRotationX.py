def setRotationX(Arg_RotationX):
    _MIN_ = -180
    _MAX_ = 180
    rotation = 0
    iters = 0
    for i in range(Arg_RotationX):
        if (rotation == _MAX_): rotation = _MIN_
        rotation += 1
        iters += 1
    print(iters)
    return rotation

def setRotationX2(Arg_RotationX):
    _MIN_ = -180
    _MAX_ = 180
    rotation = 0
    iters = 0
    for i in range(Arg_RotationX % 360):
        if (rotation == _MAX_): rotation = _MIN_
        rotation += 1
        iters += 1
    print(iters)
    return rotation

#print(setRotationX(72381))
print(setRotationX2(1000))
        
    
