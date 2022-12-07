HAPT_LABEL_TO_IND = {
    'WALKING':            1, 
    'WALKING_UPSTAIRS':   2, 
    'WALKING_DOWNSTAIRS': 3,
    'SITTING':            4, 
    'STANDING':           5,
    'LAYING':             6, 
    'STAND_TO_SIT':       7,
    'SIT_TO_STAND':       8, 
    'SIT_TO_LIE':         9, 
    'LIE_TO_SIT':         10,
    'STAND_TO_LIE':       11,
    'LIE_TO_STAND':       12
}

HAPT_IND_TO_LABEL = {v:k for k, v in HAPT_LABEL_TO_IND.items()}