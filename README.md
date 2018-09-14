# darknet-yolo-segmentation
This project is based on darknet to get image segmentation


1、compile the source code by "make -j6"



2、with the command "./darknet segmenter train the/path/to/cfg/data the/paht/to/cfg/file the/path/to/weights/files" to train on your data



3、with the command "./darknet segmenter test the/path/to/cfg/data the/paht/to/cfg/file the/path/to/weights/files the/paht/to/cfg/file the/path/to/image " to test your results，here we get https://github.com/zhengshoujian/darknet-yolo-segmentation/raw/master/pred.png



4、 run "python replay.py" to get mask，here we get https://github.com/zhengshoujian/darknet-yolo-segmentation/raw/master/mask.png

we will update our code on time, if you want to get cfg/file and weights file, please contact me by email at:2239779352@qq.com or my teammate gaoyang at:gaoyang917528@163.com
