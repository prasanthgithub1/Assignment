Overview:
1.This project places a flag image naturally on a white cloth photo using OpenCV.
2.It makes the flag look like it’s printed on the cloth instead of just pasted.

How It Works:
1.The program loads two images — one of the cloth and one of the flag.
2.It adjusts the flag’s size so it fits the cloth perfectly.
3.It reads the light and shadow of the cloth to match the flag’s brightness.
4.It shapes the flag to sit correctly on the cloth surface.
5.Finally, it blends both images together so the result looks realistic.

What You’ll Get:
After running, two images will be saved:
Warped_Flag.jpg → The flag after shape and light adjustment.
Output.jpg → The final combined image (cloth + flag).

What You Need:
Python installed
OpenCV and NumPy libraries

How to Run;
Keep your Pattern.jpg (cloth) and Flag.jpg (flag) in the same folder as the script.
Run the Python file.
Check your folder — you’ll see the final output images.

Tips:
You can replace the images with your own flag and cloth photos.
Adjust the alignment points if you want to tilt or reshape the flag.
Change blending levels for stronger or softer cloth texture.

Summary:
This project helps you combine two images realistically — showing how a flag would look when placed on a real piece of cloth.
