import pygame
import os
from settings import TILESIZE
def load_images(object_type, resize = 1):
    '''function handling loading images for objects divided by subdirs


        function takes a path as an argument and returns a dictionary of animation_type:list of frames pairs
        second argument is flag if loaded images should be resized to tilesize, to not resize set to 0
    args:
        object_type: string of objects subdir in assets
        resize: argument specifying if images should be resized to tile size, default is 1, if not pass a 0 to function
    returns:
        dictionary containing lists of all given images/animation types

    '''

    frames_to_return = {}
    path = os.path.join('.','assets', object_type)

    for animation_set in os.listdir(path):
        frames_to_return[animation_set] = []
        for frame_name in os.listdir(path + '/' + animation_set):
            if animation_set[-1] == "L":
                frame = pygame.transform.flip(
                    pygame.image.load(os.path.join(path,animation_set, frame_name)).convert_alpha(), 1, 0)
            else:
                frame = pygame.image.load(os.path.join(path,animation_set, frame_name)).convert_alpha()

            if resize:
                frame = pygame.transform.scale(frame, (TILESIZE, TILESIZE))
            frames_to_return[animation_set].append(frame)
    return frames_to_return