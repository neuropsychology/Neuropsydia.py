# -*- coding: utf-8 -*-
from .path import *
from .core import *
from .write import *



#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # --- choice ---
#version : 1.0
#to draw selectable choices.
#Authors : Dominique Makowski
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
def choice(choices=["Yes","No"], write_choices=True, overwrite_choices_display=None, choices_size=1.0, choices_color="black", y=0, height=-5, boxes_space=0.5, boxes_background_color='blue_shade', boxes_edge_color="black", boxes_edge_size=5, confirm_edge_color="orange", confirm_edge_size=3, help_list=None, help_background_color="lightgrey", title=None, title_position="default", title_x=-7.5, title_space=0.75, pictures=None, pictures_size=0.5):
    """
    Help incomplete, sorry.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - time
    """


    raw_y = y

    distance_y=height
    number = len(choices)

    if number == 2 and title_position == "default":
        title_position = "left"
    if number != 2 and title_position == "default":
        title_position = "top"
    previous_mouse_state = pygame.mouse.set_visible(True)


    list_x = [-10+boxes_space/2]
    for i in range(number-1):
        list_x.append(list_x[i]+  (20-boxes_space*number)/number + boxes_space)
    list_x2 = []
    for i in list_x:
        list_x2.append(Coordinates.to_pygame(x=i))


    coordinates = {
    'x':list_x2,
    'y':number*[Coordinates.to_pygame(y=y)],
    'width_raw':(20-boxes_space*number)/number,
    'height_raw':distance_y,
    'width':Coordinates.to_pygame(distance_x=(20-boxes_space*number)/number),
    'height':Coordinates.to_pygame(distance_y=distance_y)
    }

    if number == 2:
        coordinates = {
    'x':[Coordinates.to_pygame(x=-5.1),Coordinates.to_pygame(x=0.6)],
    'y':number*[Coordinates.to_pygame(y=y)],
    'width_raw':4.4,
    'height_raw':distance_y,
    'width':Coordinates.to_pygame(distance_x=4.4),
    'height':Coordinates.to_pygame(distance_y=distance_y)
    }

    def Display():

        for i in range(number):
            if isinstance(boxes_background_color, list) == True:
                pygame.draw.rect(screen, color(boxes_background_color[i]), (coordinates['x'][i],coordinates['y'][i],coordinates['width'],coordinates['height']),0)
            elif isinstance(color(boxes_background_color), list) == True:
                pygame.draw.rect(screen, color(boxes_background_color)[i], (coordinates['x'][i],coordinates['y'][i],coordinates['width'],coordinates['height']),0)
            else:
                pygame.draw.rect(screen, color(boxes_background_color), (coordinates['x'][i],coordinates['y'][i],coordinates['width'],coordinates['height']),0)
            if boxes_edge_size != 0:
                pygame.draw.rect(screen, color(boxes_edge_color), (coordinates['x'][i],coordinates['y'][i],coordinates['width'],coordinates['height']), boxes_edge_size)
            if write_choices is True:
                if overwrite_choices_display is None:
                    write(choices[i],x=Coordinates.from_pygame(coordinates['x'][i])+ coordinates['width_raw']/2,y=Coordinates.from_pygame(y=coordinates['y'][i])+coordinates['height_raw']/2,color=choices_color,size=choices_size)
                if isinstance(overwrite_choices_display, list):
                    write(overwrite_choices_display[i],x=Coordinates.from_pygame(coordinates['x'][i])+ coordinates['width_raw']/2,y=Coordinates.from_pygame(y=coordinates['y'][i])+coordinates['height_raw']/2,color=choices_color,size=choices_size)
            if isinstance(pictures,list):
                image(pictures[i],x=Coordinates.from_pygame(coordinates['x'][i])+ coordinates['width_raw']/2,y=Coordinates.from_pygame(y=coordinates['y'][i])+coordinates['height_raw']/2,size=pictures_size)
        if title != None:
            if title_position == 'left':
                write(title,x=title_x,y=Coordinates.from_pygame(y=coordinates['y'][0])+coordinates['height_raw']/2)
            if title_position == 'top':
                write(title,y=Coordinates.from_pygame(y=coordinates['y'][0])+title_space)
        pygame.display.flip()




    Display()
    loop = True
    while loop == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            x, y = pygame.mouse.get_pos()
            if help_list != None:
                if y > coordinates['y'][0] and y < (coordinates['y'][0]+coordinates['height']):
                        for i in range(number):
                            if x < (coordinates['x'][i]+coordinates['width']) and x > coordinates['x'][i]:
                                pygame.draw.rect(screen, color(help_background_color), (Coordinates.to_pygame(x=-10),coordinates['y'][i]+coordinates['height']+Coordinates.to_pygame(distance_y=-0.25),screen_width,Coordinates.to_pygame(distance_y=-1.50)),0)
                                write(help_list[i],y=raw_y+coordinates['height_raw']-1)
                                pygame.display.flip()



            if pygame.mouse.get_pressed()==(1,0,0):
                if y > coordinates['y'][0] and y < (coordinates['y'][0]+coordinates['height']):
                    for i in range(number):
                        if x < (coordinates['x'][i]+coordinates['width']) and x > coordinates['x'][i]:
                            response = i
                            pygame.draw.rect(screen, color(confirm_edge_color), (coordinates['x'][response],coordinates['y'][response],coordinates['width'],coordinates['height']), confirm_edge_size)
                            pygame.display.flip()
                            time.wait(100)
                            loop2 = True
                            while loop2 == True:
                                for event in pygame.event.get():
                                    if pygame.mouse.get_pressed()==(1,0,0):
                                        loop2= False
                                        loop = False
                                    if pygame.mouse.get_pressed()==(0,0,1):
                                        loop2=False
                                        Display()
#                                        pygame.draw.rect(screen, color('b'), (coordinates['x'][response],coordinates['y'][response],coordinates['width'],coordinates['height']), boxes_edge_size)
                                        pygame.display.flip()

    pygame.draw.rect(screen, color('green'), (coordinates['x'][response],coordinates['y'][response],coordinates['width'],coordinates['height']), confirm_edge_size)
    pygame.display.flip()
    pygame.mouse.set_visible(previous_mouse_state)
    return(choices[response])





