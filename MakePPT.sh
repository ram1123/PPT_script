#!/bin/bash

#	-------------------------------------------------------------------
#
#	Shell program to Make the pdf presentation using latex.
#
#	Author: 2014, Ramkrishna Sharma,,, <ramkrishna.sharma71@gmail.com>.
#	
#	The structure of the program is created by a script prodived on LinuxCommand.org
#
#	Usage:
#
#		MakePPT.sh [ -h | --help ] [-n OutPutFileName] [-f FigureType]
#
#	Options:
#
#		-h, --help		Display this help message and exit.
#		-n  OutPutFileName	Name of Output File name
#		-f  FigureType  	Type Of figure file
#
#
#	Revision History:
#
#	10/28/2014	File created by new_script ver. 2.1.0
#
#	-------------------------------------------------------------------


#	-------------------------------------------------------------------
#	Constants
#	-------------------------------------------------------------------

	PROGNAME=$(basename $0)
	VERSION="0.0.1"


	FigureType=pdf
	OutPutFileName=ppt_Comparison_WithAwithout_VBFSelection_PUIDISOonly

	nPlots=4

	MainDir=/home/ramkrishna/PhD_New_Dir_16July2016/PhysicsAnalysis/aQGC_Analysis/aQGC_Plotting_Code/TreePlotter
	#Path1=${MainDir}/Plots_El_NoCut_NoCorr_07082016_151409
	#Path2=${MainDir}/Plots_Mu_NoCut_NoCorr_07082016_151409
	Path1=${MainDir}/Plots_El_MET40_CorrPUIDISO_07082016_172220
	Path2=${MainDir}/Plots_Mu_MET40_CorrPUIDISO_07082016_172220
	Path3=${MainDir}/Plots_El_MET40_VBFWjBtag0pt8_CorrPUIDISO_07082016_174411
	Path4=${MainDir}/Plots_Mu_MET40_VBFWjBtag0pt8_CorrPUIDISO_07082016_174411

	# Imp:=>	Also, Need to modify: list*.dat So, that it takes plots in a particular order


#	-------------------------------------------------------------------
#	Functions
#	-------------------------------------------------------------------


function clean_up
{

#	-----------------------------------------------------------------------
#	Function to remove temporary files and other housekeeping
#		No arguments
#	-----------------------------------------------------------------------

	rm -f ${TEMP_FILE1}
	#rm $1.tex
}


function error_exit
{

#	-----------------------------------------------------------------------
#	Function for exit due to fatal program error
#		Accepts 1 argument:
#			string containing descriptive error message
#	-----------------------------------------------------------------------
	local err_msg

	err_msg="${PROGNAME}: ${1}"
	echo -e "\n\n${err_msg}\n\n" >&2
	#echo "${PROGNAME}: ${1:-"Unknown Error"}" >&2
	clean_up
	exit 1
}


function graceful_exit
{

#	-----------------------------------------------------------------------
#	Function called for a graceful exit
#		No arguments
#	-----------------------------------------------------------------------

	clean_up
	exit
}


function signal_exit
{

#	-----------------------------------------------------------------------
#	Function to handle termination signals
#		Accepts 1 argument:
#			signal_spec
#	-----------------------------------------------------------------------

	case $1 in
		INT)	echo "$PROGNAME: Program aborted by user" >&2
			clean_up
			exit
			;;
		TERM)	echo "$PROGNAME: Program terminated" >&2
			clean_up
			exit
			;;
		*)	error_exit "$PROGNAME: Terminating on unknown signal"
			;;
	esac
}


function make_temp_files
{

#	-----------------------------------------------------------------------
#	Function to create temporary files
#		No arguments
#	-----------------------------------------------------------------------

	# Use user's local tmp directory if it exists

	if [ -d ~/tmp ]; then
		TEMP_DIR=~/tmp
	else
		TEMP_DIR=/tmp
	fi

	# Temp file for this script, using paranoid method of creation to
	# insure that file name is not predictable.  This is for security to
	# avoid "tmp race" attacks.  If more files are needed, create using
	# the same form.

	TEMP_FILE1=$(mktemp -q "${TEMP_DIR}/${PROGNAME}.$$.XXXXXX")
	if [ "$TEMP_FILE1" = "" ]; then
		error_exit "cannot create temp file!"
	fi
}


function usage
{

#	-----------------------------------------------------------------------
#	Function to display usage message (does not exit)
#		No arguments
#	-----------------------------------------------------------------------

	echo "Usage: ${PROGNAME} [-h | --help] [-n OutPutFileName] [-f FigureType]"
}


function helptext
{

#	-----------------------------------------------------------------------
#	Function to display help message for program
#		No arguments
#	-----------------------------------------------------------------------

	local tab=$(echo -en "\t\t")

	cat <<- -EOF-

	${PROGNAME} ver. ${VERSION}
	This is a program to Make the pdf presentation using latex.

	$(usage)

	Options:

	-h, --help		Display this help message and exit.
	-n  OutPutFileName	Name of Output File name
	-f  FigureType  	Type Of figure file

	
	
-EOF-
}


#	-------------------------------------------------------------------
#	Program starts here
#	-------------------------------------------------------------------

##### Initialization And Setup #####

# Set file creation mask so that all files are created with 600 permissions.

umask 066


# Trap TERM, HUP, and INT signals and properly exit

trap "signal_exit TERM" TERM HUP
trap "signal_exit INT"  INT

# Create temporary file(s)

make_temp_files


##### Command Line Processing #####

if [ "$1" = "--help" ]; then
	helptext
	graceful_exit
fi

while getopts ":hmn:f:" opt; do
	case $opt in
		m ) echo "How many plots on one slide: "
			read nPlots;;
		n )	echo "Name of Output File name - argument = $OPTARG" 
			OutPutFileName=$OPTARG
			if [ "$OutPutFileName" == test -o "$OutPutFileName" == fig ]; then
				error_exit "Output File Name should not be fig or test."
			fi
			echo $OutPutFileName;;
		f )	echo "Type Of figure file - argument = $OPTARG" 
			FigureType=$OPTARG
			echo $FigureType;;
		h )	helptext
			graceful_exit ;;
		* )	usage
			clean_up
			exit 1
	esac
done


##### Main Logic #####

cp test.tex $OutPutFileName.tex	
count=1
if [ "$nPlots" == 4 ]; then
	#for f1 in ${Path1}/*.${FigureType}; do		#Electron SB
	#for f1 in `tac list.dat`; do		#Electron SB
	for f1 in `tac list_corrIDISOTrig_wo_SideBand.dat`; do		#Electron SB
		for f2 in ${Path2}/*.${FigureType}; do	#Electron RF
	    	filename1=$(basename  "$f1")
	    	filename1=${filename1%.*}
	    	filename1=${filename1//_/ }
	    	filename2=$(basename  "$f2")
	    	filename2=${filename2%.*}
	    	filename2=${filename2//_/ }
			if [ "${filename1}" == "${filename2}" ]; then
				for f3 in ${Path3}/*.${FigureType}; do	#Mu SB
	    			filename3=$(basename  "$f3")
	    			filename3=${filename3%.*}
	    			filename3=${filename3//_/ }
					if [ "${filename1}" == "${filename3}" ]; then
						for f4 in ${Path4}/*.${FigureType}; do	#Mu FR
	    					filename4=$(basename  "$f4")
	    					filename4=${filename4%.*}
	    					filename4=${filename4//_/ }
							if [ "${filename1}" == "${filename4}" ]; then
								sed  "s|fig1|$f1|g; s|fig2|$f2|g; s|fig3|$f3|g; s|fig4|$f4|g; s|TitleFrame|$filename1|g" fig_four.tex	> fig_$count.tex 
								sed -i "/Pointer-rk/r fig_$count.tex" "$OutPutFileName.tex"
								echo "${filename1}  ${filename2}  ${filename3}  ${filename4}"
								((++count))
							fi
						done
					fi
				done
			fi
		done
	done
elif [ "$nPlots" == 2 ]; then
	#for f1 in ${Path1}/*.${FigureType}; do		#Electron SB
	#for f1 in `tac list.dat`; do		#Electron SB
	for f1 in `tac list_corrIDISO.dat`; do		#Electron SB
		for f2 in ${Path2}/*.${FigureType}; do	#Electron RF
	    	filename1=$(basename  "$f1")
	    	filename1=${filename1%.*}
	    	filename1=${filename1//_/ }
	    	filename2=$(basename  "$f2")
	    	filename2=${filename2%.*}
	    	filename2=${filename2//_/ }
			if [ "${filename1}" == "${filename2}" ]; then
				sed  "s|fig1|$f1|g; s|fig2|$f2|g; s|TitleFrame|$filename1|g" fig_two.tex	> fig_$count.tex 
				sed -i "/Pointer-rk/r fig_$count.tex" "$OutPutFileName.tex"
				echo "${filename1}  ${filename2}"
				((++count))
			fi
		done
	done
fi
pdflatex $OutPutFileName.tex
pdflatex $OutPutFileName.tex
rm  $OutPutFileName.toc $OutPutFileName.snm $OutPutFileName.out $OutPutFileName.nav $OutPutFileName.aux $OutPutFileName.log
rm fig_[0-9][0-9].tex
rm fig_[0-9].tex
gnome-open $OutPutFileName.pdf &
echo "Finished."

graceful_exit
