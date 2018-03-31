float setRotationX(Arg_RotationX)
{
    int _MIN_ = -180;
    int _MAX_ = 180;
    float rotation = 0;
    for (int i = 0; i > Arg_RotationX % 360; ++i)
    {
        if (rotation == _MAX_) { rotation = _MIN_;}
        rotation += 1;
    }
    return rotation;
}