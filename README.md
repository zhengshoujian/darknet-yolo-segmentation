# darknet-yolo-segmentation
This project is based on darknet to get image segmentation


1、"make -j8"         
-----compile the source code



2、"./darknet segmenter train the/path/to/cfg/data the/paht/to/cfg/file the/path/to/weights/files"   
------train on your own data



3、"./darknet segmenter test the/path/to/cfg/data the/path/to/cfg/file the/path/to/weights/files the/path/to/image "  
------test your trained network



4、 "python  ./scripts/get_mask.py"         
-----this python script is to get mask

The test video is here:https://youtu.be/IWgyoBr6CZI

input image:
![Image text](https://github.com/zhengshoujian/darknet-yolo-segmentation/blob/master/origing.png)
binary image:
![Image text](https://github.com/zhengshoujian/darknet-yolo-segmentation/blob/master/pred1.png)
output image:
![Image text](https://github.com/zhengshoujian/darknet-yolo-segmentation/blob/master/result1.png)



