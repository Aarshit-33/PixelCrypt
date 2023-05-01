Project Title: Message hiding inside image using image processing.

Team Members: 
1] Azim Baldiwala (22BCE502)
2] Arshit Jolapara (22BCE510)

--------------------------------------------------------------------------------------

=>> The project is divided into 2 major part:
1] Lossy endcoding and decoding
2] Lossless encoding and decoding 


=>> Description: 

=> 1] Lossy endcoding and decoding

- Hide Message an Image file, (PNG) File using LSB method.

- It converts the message into bits and then hides it inside the image.

- Traverse to every pixel and then edit the LSB of each "r", "g" and "b" of the pixel with the message bit. Append end delimeters at the end to denote end of the message.

- Decoding is also done in similar manner.

- Advantage of lossy method:

1] Fast and reccommend for small messsages.
2] Easy to implement 

- Disadvantages of lossy method:

1] Image may have noticable change if the message is long.

-----------------------

=> 2] LossLess encoding and decoding.

- It is similar to the lossy method the only difference is it randomly selects the pixels in which the message bits are to be hidden.

- It generates a random number (using random seed) on a key value provided by the user at the time of encoding.

- The same key value is required at the time of decoding the image.

- Advantage of Lossless method:

1] does not change the image 
2] decoding is not possible without the original key

- Disadvantage of Lossless method:

1] difficult to implement

--------------------------------------------------------------------------------------

=>> Dependencies :

Python 3.5 or later 
Flask (python framework)
Pillow (image processing lib)
Python-opencv (image processing)
Numpy

--------------------------------------------------------------------------------------

=>> The Project contains several file :

1] app.py : It has all the web routes. It is the backend file for the flask.
2] hide_lossy.py: This file is used to hide the message inside the image using lossy method.
3] hide_lossless.py: This file is used to hide the message inside the image using lossyless method.
4] templates directory has all the html files of the GUI
5] static directory has all the server data such as user input images and the GUI dependencies.
6] Sample_images:  Contains sample image dataset

--------------------------------------------------------------------------------------

=>> How to run the project.

Method 1: Using  the flask GUI
Simply run the "app.py" and then open the following link on any web browser "localhost:5000"

Method 2: Using Console 
Open Cmd and execute the "hide_lossy.py" or "hide_lossless.py"
They will also work as a console applications.

ThankYou!

 

