The task requires psychopy/python 3

You may use Matching.bat to open the task
First, edit the file by providing the path to the task's folder

The task’s parameters can be set in config.yaml.
The default visual parameters such as stimuli size, need to be adjusted to the specific screen size and resolution.
The task’s instruction is prepared in .png files, whichc can be modified using the instruction.pptx files (in the ‘images’ folder). 
To use a plain text instruction provide a .txt file into ‘messages’ and load the file using show_info() function (see #INSTRUCTIONS in main.py).

The \data\items.csv contains the list of items, which can be modified, removed or added:

FEED – feedback displayed or not

TRAIN – training or experimental item

VA – provides positions (from 0 to 8) of vertices on a 3x3 virtual matrix of the A graph (the left graph):
0 1 2
3 4 5
5 7 8

EA – list of ordered pairs defining edges between the given vertices of the A graph; bidirectional edges are possible; 
	edges can only link neighbouring vertices (e.g. 8 can be linked only with 4,5 and 7)

left – defines a pair of corresponding vertices to be matched using the left mouse button; 
	first digit in the pair reflects a vertex in the graph A, and the second digit reflects a vertex in the graph B; 

right - defines a pair of corresponding vertices to be matched using the right mouse button; 
	first digit in the pair reflects a vertex in the graph A, and the second digit reflects a vertex in the graph B; 


