import pygame
import os

def load_images(object_type):
    '''returns dictionary of animation frames

    function takes a path as an argument and returns a dictionary of animation_type:list of frames pairs
    '''

    frames_to_return = {}
    path = os.path.join('.','assets', object_type)
    # path = './assets/' + object_type
    # for _, animation_sets, frames in walk(path):
    #     for animation_set in animation_sets:
    #         print(animation_set)
    #         for frame in frames:
    #             print(frame)

    for animation_set in os.listdir(path):
        frames_to_return[animation_set] = []
        print(animation_set)
        for frame_name in os.listdir(path + '/' + animation_set):
            if animation_set[-1] == "L":
                # frame = pygame.transform.flip(pygame.image.load(path + animation_set + '/' + frame_name).convert_alpha(), 1, 0)
                frame = pygame.transform.flip(
                    pygame.image.load(os.path.join(path,animation_set, frame_name)).convert_alpha(), 1, 0)
            else:
                # frame = pygame.image.load(path + '/' + animation_set + '/' + frame_name).convert_alpha()
                frame = pygame.image.load(os.path.join(path,animation_set, frame_name)).convert_alpha()
            frames_to_return[animation_set].append(frame)

        # for animation in animation_sets:
        #     frames_to_return[animation_set] = []
        #     for frame_name in frames_names:
        #         # all images in assets faces right so a flip is needed
        #         if animation_set[-1] == "L":
        #             frame = pygame.transform.flip(pygame.image.load('./assets/frames/' + frame_name).convert_alpha(), 1, 0)
        #         else:
        #             frame = pygame.image.load('./assets/frames/' + frame_name).convert_alpha()
        #         frames_to_return[animation_set].append(frame)
    return frames_to_return