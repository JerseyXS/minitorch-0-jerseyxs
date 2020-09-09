from project.datasets import Simple, Split, Xor

def classifySimple(pt):
    "Classify based on x position"
    if pt[0] < 0.54:
        return 1.0
    else:
        return 0


def classifySplit(pt):
    "Classify based on x position"
    if pt[0] < 0.26:
        return 1.0
    elif pt[0] >= 0.26 and pt[0] <= 0.77:
        return 0
    else:
        return 1.0


def classifyXor(pt):
    "Classify based on x and y position"
    if pt[0] < 0.48 and pt[1] > 0.47:
      return 1.0
    elif pt[0] > 0.48 and pt[1] < 0.47:
      return 1.0
    else:
      return 0


N = 100
Simple(N, vis=True).graph("initial", model=classifySimple)
# # Split(N, vis=True).graph("Split", model=classifySplit)
# Xor(N, vis=True).graph("Xor", model=classifyXor)