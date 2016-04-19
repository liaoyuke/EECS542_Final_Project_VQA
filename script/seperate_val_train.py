def write_objs(img_list, output, map):
	with open(img_list) as f_img:
		img_lines = f_img.readlines()
	f_out = open(output, 'w')
	for img in img_lines:
		img = img.rstrip()
		print img
		obj = map[img]
		f_out.write(obj + '\n')
	f_out.close()


trainval_imglist_file_path = '../data/coco_trainval2014_imglist.txt'
trainval_train_imglist_file_path = '../data/coco_trainval2014_train_imglist.txt'
trainval_val_imglist_file_path = '../data/coco_trainval2014_val_imglist.txt'

obj_folder_path = '/Users/lidin/Documents/EECS542/EECS542_Final_Project/EECS542_Final_Project_VQA/code/concept_extraction/Text_Parsing/objects/'
trainval_obj_file_path = obj_folder_path + 'coco_trainval2014_objects_stem.txt'

trainval_train_obj_file_path = obj_folder_path + 'coco_trainval2014_train_objects_stem.txt'
trainval_val_obj_file_path = obj_folder_path + 'coco_trainval2014_val_objects_stem.txt'

img_to_obj = {}

with open(trainval_obj_file_path) as f_obj:
		obj_lines = f_obj.readlines()
with open(trainval_imglist_file_path) as f_img:
		img_lines = f_img.readlines()

for obj_line, img_line in zip(obj_lines, img_lines):
	obj_line = obj_line.rstrip()
	img_line = img_line.rstrip()
	img_to_obj[img_line] = obj_line

write_objs(trainval_train_imglist_file_path, trainval_train_obj_file_path, img_to_obj)
write_objs(trainval_val_imglist_file_path, trainval_val_obj_file_path, img_to_obj)





