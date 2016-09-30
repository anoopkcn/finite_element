def get_mesh():
    param = open("parameters.txt", 'r')
    for line in param :
        l = line.split()
        if len(l) < 2 :
            continue;
        if l[0] == "mesh" and l[1] == "=" :
            mesh_name = l[2]
            break;
    param.close()
    return mesh_name

def get_force():
    param = open("parameters.txt", 'r')
    for line in param :
        l = line.split()
        if len(l) < 2 :
            continue;
        if l[0] == "force" and l[1] == "=" :
            force = l[2]
            break;
    param.close()
    return force
