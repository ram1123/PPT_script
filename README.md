# How To Use This Script
1. Do git clone the script
	**$git clone https://github.com/ram1123/PPT_script.git**

2. Above command will create a directory named **PPT_Script**

3. Put all of your plot file in this directory. **Please name the plots as you want the heading of the slide. Because the name of file will become the heading of slide**

4. Now Run the command
	**./MakePPT.sh**

5. But by default it will take only \*.pdf files only

6. If you want to use any other format then use **-f** option of the script
	**./MakePPT.sh -f jpg
	or
	./MakePPT.sh -f jpeg**

7. Also by default it will make a pdf file named **ppt_test.pdf**
8. If you want to get any other name then you can use **-n** option of the script
	**./MakePPT.sh -n ram**
	
   Then it will create output pdf file with name **ram.pdf**

9. If you want to do both things at a time, i.e. change the file format to recognize and name of output file then you can use both option like
	**./MakePPT.sh -f jpeg -n ram**

