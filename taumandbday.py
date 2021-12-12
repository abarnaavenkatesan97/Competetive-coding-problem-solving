def taumbday(b,w,bc,wc,z):
    cost = 0
    if bc == wc:
        cost = (b * bc) + (w * wc)
    elif (z > bc) and (z > wc):
        cost = (b * bc) + (w * wc)
    elif wc < bc:
        cost = b * z
        cost = cost + ((b + w) * wc)
        if ((b * bc) + (w * wc)) < cost:
            cost = (b * bc) + (w * wc)
    elif bc < wc:
        cost = w * z
        cost = cost + ((b + w) * bc)
        if ((b * bc) + (w * wc)) < cost:
            cost = (b * bc) + (w * wc)
    return cost
b,w,bc,wc,z = 4,3,5,7,3
print(taumbday(b,w,bc,wc,z))
