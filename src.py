
from projects.pyhuskylens import HuskyLens, ALGORITHM_OBJECT_CLASSIFICATION, clamp_int, ALGORITHM_COLOR_RECOGNITION
from hub import button
from spike import Motor

motorfront = Motor('A')
motor = Motor('B')

setspeedfront = int(-30)
setspeedturn = int(10)
# motorfront.start()

motor.start(setspeedfront)
motorfront.run_to_position(0)

hl = HuskyLens('F', debug=False)

# เขียว = 1 เลี้ยวซ้าย
# แดง = 2 เลี้ยวขวา

# ล้อหน้า = A
# ล้อหลัง = B

# Get x/y loc of a face
print("Starting face recognition")
hl.set_alg(ALGORITHM_COLOR_RECOGNITION)




while True:
    blocks = hl.get_blocks()
    print(blocks)
    if len(blocks) > 0:
        if blocks[0].ID == 1:
            pass
            # print(blocks)
            # motorfront.run_for_rotations(0.25,setspeedturn)
            if blocks[0].width >= 90:
                # motor.stop()
                motorfront.run_for_rotations(0.1)
                motorfront.run_to_position(0)
                motorfront.run_for_rotations(-0.1)
                motorfront.run_to_position(0)
                motor.stop()
                # break

        


# hl.set_alg(ALGORITHM_OBJECT_CLASSIFICATION)
# motorfront.run_for_rotations(0.01, 100)
# print(motorfront.get_degrees_counted())
# while True:
#     blocks = hl.get_blocks()
#     print(blocks)
#     if len(blocks) > 0:

#         face_x = blocks[0].x
#         error_x = (face_x-155)
        # print(error_x)
        # speed_x = 100 if error_x > 0 else -100
        # motorfront.run_for_rotations((error_x)//10,-100)
        # speed_x = -100 if error_x > 0 else 100
        # motorfront.run_for_degrees(clamp_int(error_x*0.2), speed_x)
        # motorfront.run_for_degrees(clamp_int(error_x*0.2), speed_x)

# while not button.right.is_pressed():
#     blocks = hl.get_blocks()
#     print(blocks)
#     if len(blocks) > 0:
        
#         face_y = blocks[0].y
#         error_y = (face_y-120)
#         speed_y = 100 if error_y > 0 else -100
#         motorfront.run_for_degrees(clamp_int(error_y*0.1), speed_y)

    #     if blocks[0].ID == 1:
    #     #    print("1")
    #        motorfront.run_for_rotations(0.25,setspeedturn)
    #    elif blocks[0].ID == 2:
    #     #    print("2")
    #        motorfront.run_for_rotations(-0.25,setspeedturn)
        # else:
        #    print("error")
    # else:
    #    print("error")
    # print(blocks)
