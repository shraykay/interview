time = raw_input()
time = time.split(':')

hour = float(time[0])
minutes = float(time[1])

hour = hour % 12

degrees = 360

hourDegree = ((hour * 60 + minutes) / 720) * 360
minuteDegree = float(minutes * degrees/60)

#print hourDegree, minuteDegree

angle = abs(hourDegree-minuteDegree)
outsideAngle = 360-angle
print min(angle,outsideAngle)