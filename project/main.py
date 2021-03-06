from obj.Form import Form
from obj.Image import Image
import cv2

form = Form('data/3.jpg')
form.text_detection()
form.element_detection()
form.visualize_all_elements()

form.textbox_recognition()
form.visualize_all_elements()

form.group_elements_to_units()
form.visualize_units()

form.input_compound_recognition()
form.visualize_inputs()

# board = form.img.img.copy()

# ******* show sorted elements ********
# elements = form.sort_elements(direction='v')
# for ele in elements:
#     print(ele.location)
#     ele.visualize_element(board)
#     cv2.imshow('b', board)
#     cv2.waitKey()

# ******* show elements relationship ********
# for text in form.texts:
#     board = form.img.img.copy()
#     for rec in form.rectangles:
#         if text.element_relation(rec) != 0:
#             text.visualize_element(board, (0,255,0), 2)
#             rec.visualize_element(board, (0,0,255),2, show=True)
