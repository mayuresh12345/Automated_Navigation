# Automated_Navigation
### Abstract
Lane recognition is one of the key technologies in the field of autonomous vehicles. It is widely used in assisted driving systems, lane departure warning systems and vehicle collision prevention system, and it has great significance in improving traffic safety. 

### Steps for lane detection in an image -
1. I converted the image to gray scale to detect edges in the image. 

2. Whenever there is an edge the pixel intensity changes rapidly (from 0 to 255) which we want to detect. But before doing so, we should make the edges smoother. The gray scale image has many rough edges which caused many noisy edges to be detected. So Gaussian Blur is applied to make the edges smoother.
 
3. Used canny edge detection to detect gradient in image and plotted the image using Matplotlib library to get the coordinates of region of     interest. 

4. Used Hough Line Transform & collected positive slope lines and negative slope lines separately and
took their averages. 

5. Finally, used weights to superimpose the detected lane image on original image.

### Steps for mask generation
1. I implemented a VGG16 model for segmentation using Keras library

2. Trained the model on KITTI dataset for 100 epochs

3. After each epoch, the weights get saved in Road-Segmentation/trained_model/trained_model.h5

4. The trained model was used to predict the segmentation masks. For each segmentation mask, the region between detected lanes was extracted and saved as a mask image.

5. I superimposed the mask image on original image to get the segmented roi with detected lanes.

I applied the same principle to a video by extracting each frame and performing above mentioned operations
