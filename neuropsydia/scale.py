# -*- coding: utf-8 -*-
from .path import *
from .core import *
from .image import *
from .write import *
from .miscellaneous import *


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def scale_styles():
    """
    Returns available scale styles.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> print(n.scale_styles())
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)
    """
    styles = os.listdir(Path.binary())
    styles = [x for x in styles if "cursor_" in x ]
    styles = [x for x in styles if not "_validated" in x ]
    styles = [x.replace('cursor_', '') for x in styles]
    styles = [x.replace('.png', '') for x in styles]
    return(styles)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def scale(style='red', x=0, y=-3.3, anchors=None, anchors_space=2, anchors_size=0.7, edges=[0, 100], validation=True, analog=True, step=1, labels="numeric", labels_size=0.8, labels_rotation=0, labels_space=-1, labels_x=0, line_thickness=4, line_length=8, line_color="black", background="white", title=None, title_style="body", title_size=1, title_space=1.75, point_center=False, point_edges=True, reverse=False, force_separation=False, separation_labels=None, separation_labels_size=1, separation_labels_rotate=0, separation_labels_space=-1, show_result=False, show_result_shape="circle", show_result_shape_fill_color="white", show_result_shape_line_color="black", show_result_shape_size=0.8, show_result_space=1.25, show_result_size=0.5, show_result_color="black", show_result_decimals=1, cursor_size=1):
    """
    Draw a scale.

    Parameters
    ----------
    style : str
        style, check `neuropsydia.scale_styles()` function to see what's available.
    x : float
        Horizontal position of the center (from -10 (left) to 10 (right)).
    y : float
        Vertical position of the center (from -10 (bottom) to 10 (top)).
    anchors : list of two str
        a list of two propositions to be displayed on the sides of the scale (e.g., [not at all, very much]).
    anchors_space : float
        spacing betweeen the edge and the anchors.
    anchors_size : float
        size of the anchors' font.
    edges : list
        the underlying numerical edges of the scale.
    validation : bool
        confirm the response with a second left click or withdraw with a right click.
    analog : bool
        continuous (discrete) scale.
    step : int
        if analog is True, what are the step to go between the edges (determine the number of points on the scale).
    labels : str or list
        "num", "numeric" or "numbers" or list of actual text labels (e.g., ["not at all", "a bit", "very much"]).
    labels_size : float
        Size of labels.
    labels_rotation : float
        Labels rotation angle.
    labels_space : float
        Space between scale and labels.
    labels_x : float
        Horizontal dodging position.
    line_thickness : float
        Scale line thickness.
    line_length : float
        Scale line length.
    line_color : str
        Scale line color.
    background : str
        Scale background color.
    title : str
        Scale title/question to ask.
    title_style : str
        'body', 'psychometry', 'psychometry_bold', 'light', 'bold'. You can also insert the name of a system font, or the path to a specific font.
    title_size : float
        Title size.
    title_space : float
        Space between scale and title.
    point_center : bool
        Place a point at the center.
    point_edges : bool
        Place points at the edges.
    reverse : bool
        The result is scored as inverse.
    force_separation : int
        Creates visual separations with points.
    separation_labels : list
        Place labels corresponding to the separations.
    separation_labels_size : float
        Separation labels size.
    separation_labels_rotate : float
        Separation labels rotation angle.
    separation_labels_space : float
        Space between scale and separation labels.
    show_result : bool
        Add a marker to show the value on scale.
    show_result_shape : str
        Shape of this marker. "circle" or "rectangle".
    show_result_shape_fill_color : str
        Fill color of the marker.
    show_result_shape_line_color : str
        Line color of the marker.
    show_result_shape_size : float
        Marker's shape size.
    show_result_space : float
        Space between scale and marker.
    show_result_size : float
        Results text size.
    show_result_color : str
        Results text color.
    show_result_decimals : int
        How many decimals to show.
    cursor_size : float
        Size of the circle cursor.

    Returns
    ----------
    response : float
        Response value.

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> response = n.scale()
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    """
    pygame.mouse.set_visible(True)
    # Debugging
    styles_list = scale_styles()
    if style not in styles_list:
        print("NEUROPSYDIA ERROR: scale(): wrong style (check available styles with the scale_styles() function")
        style = "red"

    # change the parameters according  to the style
    cursor_name = 'cursor_' + style + ".png"
    if style == "absorption":
        anchors_space = 3
        anchors = ["Très distant(e)", "Très absorbé(e)"]


    # Coordinates calculating
    line_length_raw = Coordinates.to_pygame(distance_x = line_length)
    scale_y = y  # because y will be further used for the mouse position
    scale_y_raw = Coordinates.to_pygame(y = y) #expressed in pygame's coordinates

    scale_x = x  # center x of the scale
    edge_left = x - line_length /2
    edge_right = x + line_length /2
    edge_left_raw = Coordinates.to_pygame(x = edge_left)
    edge_right_raw = Coordinates.to_pygame(x = edge_right)
    cursor_x = scale_x
    cursor_y = scale_y

    if analog == False:
        #initialize the position and label list
        point_list_range = range(len(range(edges[0],edges[1],step))+1) #is the number of elements in order
        points_position = []
        points_position_raw = [] #positions for points in order to ease the fixation of the cursor
        label_list = []
        #calculate them
        for i in point_list_range:
            points_position.append(edge_left + i*line_length/len(range(edges[0],edges[1],step)))
            points_position_raw.append(edge_left_raw + i*line_length_raw/len(range(edges[0],edges[1],step)))
            if labels == "numeric" or labels == "num" or labels == "numbers":
                label_list.append(str(i))
            elif isinstance(labels, list):
                if len(labels) == len(point_list_range):
                    label_list.append(labels[i])
                else:
                    print("NEUROPSYDIA ERROR: scale(): wrong labels length")
            else:
                print("NEUROPSYDIA ERROR: scale(): labels argument requires a list")

    if separation_labels != None:
        if isinstance(separation_labels, list):
            if force_separation is False:
                force_separation = len(separation_labels)

    def draw_all():
        #Draw the mask
        rectangle(x=scale_x, y=scale_y, width=line_length + anchors_space + 8, height=2, line_color=background, thickness=0, fill_color=background, opacity=225)
        if analog is False:
            rectangle(x=scale_x, y=scale_y + labels_space, width=line_length + anchors_space + 1,height=3, line_color=background, thickness=0,fill_color=background,opacity=225)
        if title != None:
            rectangle(x=scale_x, y=scale_y + title_space, width=line_length*2,height=1,line_color=background,thickness=0,fill_color=background,opacity=225)
        if show_result is True:
            rectangle(x=scale_x, y=y-show_result_space,width=line_length + anchors_space + 8,height=show_result_shape_size+0.7, line_color=background, thickness=0, fill_color=background, opacity=225)
#        Draw the line
        pygame.draw.line(screen, color(line_color), [edge_left_raw,scale_y_raw], [edge_right_raw,scale_y_raw], line_thickness)
        if style == "absorption":
            image('absorption_man.png',x=scale_x, y=scale_y,size=1.3, path=Path.binary())
            image('absorption_desk.png',x=edge_right,y=scale_y,size=1.3, path=Path.binary())
        #draw the anchors
        if anchors != None:
            write(anchors[0], size = anchors_size, x = edge_left - anchors_space,y= scale_y)
            write(anchors[1], size = anchors_size, x = edge_right + anchors_space,y= scale_y)
        #display the points and the labels
        if analog == False:
            for i in point_list_range:
                image('scale_point.png', x=points_position[i], y=scale_y, size=0.25, path=Path.binary())
                write(label_list[i], x=points_position[i]+labels_x, y=scale_y + labels_space, size=labels_size,rotate=labels_rotation)
        else:
            if point_center == True:
                image('scale_point.png', x=scale_x, y=scale_y, size=0.25, path=Path.binary())
            if point_edges == True:
                image('scale_point.png', x=edge_left, y=scale_y, size=0.25, path=Path.binary())
                image('scale_point.png', x=edge_right, y=scale_y, size=0.25, path=Path.binary())
        if separation_labels != None:
            if isinstance(separation_labels, list):
                for i in range(len(separation_labels)):
                    write(separation_labels[i], x=edge_left + line_length/force_separation*(i+1) - line_length/force_separation/2, y=scale_y+separation_labels_space, size=separation_labels_size, rotate=separation_labels_rotate)
            else:
                print("NEUROPSYDIA ERROR: scale(): separation_labels requires a list")
        if force_separation is False:
            if isinstance(force_separation, int):
                for i in range(force_separation-1):
                    image('scale_point.png', x=edge_left + line_length/force_separation*(i+1), y=scale_y, size=0.25)
            else:
                print("NEUROPSYDIA ERROR: scale(): force_separation requires a integer")
        if title != None:
            write(title, title_style, size=title_size, x=scale_x, y=scale_y + title_space)
        image(cursor_name, x=cursor_x, y=scale_y, size=cursor_size, path=Path.binary())
        if show_result is True:
            if show_result_shape == "circle":
                circle(x=cursor_x, y=y-show_result_space, size=show_result_shape_size, fill_color=show_result_shape_fill_color, line_color=show_result_shape_line_color)
            if show_result_shape == "rectangle":
                rectangle(x=cursor_x, y=y-show_result_space, width=show_result_shape_size, height=show_result_shape_size, fill_color=show_result_shape_fill_color, line_color=show_result_shape_line_color)
            if show_result_decimals == 0:
                write("%.0f" %(edges[0] + (cursor_x - edge_left)*(edges[1]-edges[0])/line_length), x=cursor_x, y=y-show_result_space, size=show_result_size, color=show_result_color)
            if show_result_decimals == 1:
                write("%.1f" %(edges[0] + (cursor_x - edge_left)*(edges[1]-edges[0])/line_length), x=cursor_x, y=y-show_result_space, size=show_result_size, color=show_result_color)
            if show_result_decimals == 2:
                write("%.2f" %(edges[0] + (cursor_x - edge_left)*(edges[1]-edges[0])/line_length), x=cursor_x, y=y-show_result_space, size=show_result_size, color=show_result_color)
        refresh()
    pygame.event.set_allowed(pygame.KEYDOWN)


    draw_all()
    loop=True
    while loop is True:
        for event in pygame.event.get(): #for each event...
            cursor_x_raw, cursor_y_raw = pygame.mouse.get_pos()  #.get mouse position
            cursor_x, cursor_y = Coordinates.from_pygame(x=cursor_x_raw, y=cursor_y_raw)  # convert the raw position


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return(np.nan)
                if event.key in keys["normal"]:
                    if keys["normal"][event.key] == "LEFT" or keys["normal"][event.key] == "RIGHT":
                        pygame.event.set_blocked(pygame.KEYDOWN)
                        return(keys["normal"][event.key])
            if cursor_y < scale_y+2 and cursor_y > scale_y-2:
                if cursor_x < edge_right + 2 and  cursor_x > edge_left - 2:
                    #fix the x
                    if cursor_x < edge_left:
                        cursor_x = edge_left
                    if cursor_x > edge_right:
                        cursor_x = edge_right
                    if analog == False:
                        cursor_x = min(points_position, key=lambda a:abs(a-cursor_x))

                    draw_all()

                    if pygame.mouse.get_pressed()==(1,0,0):
                        #convert the  real ratio into the reponse
                        response = edges[0] + (cursor_x - edge_left)*(edges[1]-edges[0])/line_length

                        #what happened when validation is on
                        if validation == True:
                            cursor_name = 'cursor_' + style + '_validated.png'
                            draw_all()

                            mouse_pressed = True
                            while mouse_pressed == True:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            return(np.nan)
                                        if event.key in keys["normal"]:
                                            if keys["normal"][event.key] == "LEFT" or keys["normal"][event.key] == "RIGHT":
                                                pygame.event.set_blocked(pygame.KEYDOWN)
                                                return(keys["normal"][event.key])
                                    if pygame.mouse.get_pressed()==(1,0,0):
                                        time.wait(100)
                                        mouse_pressed = False
                                        loop = False
                                    if pygame.mouse.get_pressed()==(0,0,1):
                                        cursor_name = 'cursor_' + style + '.png'
                                        mouse_pressed = False
    if reverse == True:
        response = -1*(response - (edges[0]+edges[1]))
    pygame.mouse.set_visible(False)
    pygame.event.set_blocked(pygame.KEYDOWN)
    return(response)