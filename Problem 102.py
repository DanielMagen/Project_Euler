line_crosses_positive_x = 1
line_crosses_negative_x = -1
line_crosses_origin = 2
line_doesnt_cross_x = 0

def line_crosses_x(p1, p2):
    """
    :return: if the line crosses the positive x axis it returns 1
    if the line crosses the negative x axis it returns -1
    if the line does not cross the x axis it returns 0
    
    if the line crosses the origin it returns 2
    
    cant handle horizontal lines
    """
    a, b = p1
    c, d = p2
    t = -b/(d-b)
    if t < 0 or t > 1:
        return line_doesnt_cross_x

    x_coordinate_of_cut = a+t*(c-a)

    if x_coordinate_of_cut == 0:
        return line_crosses_origin

    if x_coordinate_of_cut > 0:
        return line_crosses_positive_x

    return line_crosses_negative_x


def line_is_horizontal(p1, p2):
    return p1[1] == p2[1]

def horizontal_line_contains_origin(p1, p2):
    if p1[1] != 0:
        return False

    if p1[0] == 0 or p2[0] == 0:
        return True

    if p1[0] > 0 and p2[0] < 0:
        return True

    if p1[0] < 0 and p2[0] > 0:
        return True

    return False

def triangle_contains_origin(triangle_coordinates):
    # handle the case when the triangle contains straight horizontal line
    # right on the x axis
    line1 = [triangle_coordinates[0], triangle_coordinates[1]]
    line2 = [triangle_coordinates[0], triangle_coordinates[2]]
    line3 = [triangle_coordinates[1], triangle_coordinates[2]]
    lines = [line1, line2, line3]

    results = []
    for line in lines:
        p1 = line[0]
        p2 = line[1]
        if line_is_horizontal(p1, p2):
            if horizontal_line_contains_origin(p1, p2):
                return True
            continue
        cross = line_crosses_x(p1, p2)
        if cross == line_crosses_origin:
            return True
        results.append(cross)

    return line_crosses_positive_x in results and line_crosses_negative_x in results

def triangle_coordinates_to_lines(triangle):
    p1 = [triangle[0],triangle[1]]
    p2 = [triangle[2], triangle[3]]
    p3 = [triangle[4], triangle[5]]
    return [p1, p2, p3]

triangles = [None] # file in the site result was 228

count = 0
for triangle in triangles:
    contains_o = triangle_contains_origin(triangle_coordinates_to_lines(triangle))
    if contains_o:
        count += 1

print(count)
