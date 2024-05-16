# LC3-bad-apple
LC3 is best system to printout bad apple

# little programs
* download_vedio
download vedio as ./vedio.mp4

* convert_vedio_2_frame.py
make ./vedio.mp4 as bunch of frames
frames will be saved like ./images/000000.jpg, ./images/000001.jpg, ...

* convert_frame_2_array.py
transform frame image to black/white array. 0 for black and 1 for white
save the list at ./raw_array.pickle

* convert_array_2_xor.py
make raw array to xor array. xor[i] = array[i-1] ^ array[i]
save the list at ./xor_array.pickle

* make_flipflop.py
refine xor array. Write where to be flipted
['3f', '5a'] means pixel 3f and 5a should be flipted at this frame, compare to previous one.
save the list at ./fflop.pickle

* make_asm
make LC3 assembly data code ./asm.txt from ./fflop.pickle

# code
the code will run in LC3 simulator.
This code was tested and run on LC3Tools-2.0.2, made by Richard So.