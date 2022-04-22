import random

R_FEVER = "Prefer Paracetamol,and take rest"
R_BODYACHE = "Take Dolo650"


def unknown():
    response = ["Could you please resay that? ",
                "...",
                ][
        random.randrange(2)]
    return response