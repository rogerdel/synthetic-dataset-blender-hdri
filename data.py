# Initial data
"""
bag
bottle
container
cup
gloves
spoon
straw
"""
collection_start  = 'bag'
collection_end    = 'straw'
images_per_class = 1
filenameSize     = 10
saveDir          = 'D:/dataset_shyntethic'
hdrisDIr         = 'D:/Devs/python/synthetic-dataset-blender-hdri/HDRIS'
prob_many_objs   = 0.3
prob_add_obj     = 0.5

# transformation
# scale
prob_scale       = 0.9
scale_min        = 1
scale_max        = 2

# rotation (x, y, z) between -360 and 360
prob_roate       = 0.55
minrot           = [-80, 0, -80]
maxrot           = [80, 360, 80]

# HDRI
min_hdri_rotation = [-45, 0 , 0]
max_hdri_rotation = [15,  0,  360]

# Camera
common_resolutions = [(852,480), (1280,720), (1920, 1080)]
high_resolutions   = [(2048, 1080), (2560, 1440), (4096, 2160)]
prob_common_res    = 0.6
prob_high_res      = 0.05
prob_flip_res      = 0.3 

objData = {
    'bag': {
        'garbagebags': 0.1,
        'transparent bag': 0.7
    },
    'bottle': {
        'Plastic_transparent': 0.3,
        'lid': 1,
        'label': 1,
        'inner label': 0,
        'no_label_prob': 0.1
    },
    'container': {
        'Plastic_transparent': 0.005,
    },
    'cup': {
        'Plastic_transparent': 0.005
    },
    'gloves': {
        'gloves': 0.8,
        'colors' : [[0.238398, 0.341915, 0.904661], [0.208637, 0.558341, 0.930111], [0.027321, 0.114435, 0.327778], [0.871367, 0.83077, 0.708376]]
    },
    'spoon': {
        'spoon': 0.5,
    },
    'straw': {
        'straw': 1,
    }
}
