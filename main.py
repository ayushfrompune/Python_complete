boxes = int(input("Enter no. of boxes: "))
robots = int(input("Enter no. of robots: "))
box = []
for i in range(boxes):
    box.append("close")

for a in range(1,robots+1):
    for i in range(1,boxes+1):
        if i%a==0:
            b = i - 1
            if b+1!=boxes:
                if box[b]=="close":
                    box.pop(b)
                    box.insert(b, 'open')
                elif box[b] == "open":
                    box.pop(b)
                    box.insert(b, "close")
            elif b+1 ==boxes:
                if box[b]=="close":
                    box.pop()
                    box.append("open")
                elif box[b] == "open":
                    box.pop()
                    box.append("close")
        else:
            continue
print(box)
